from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from openpyxl import load_workbook
from museos.models import Museo

class Command(BaseCommand):
    help = "Importa o actualiza museos desde data/museos.xlsx"

    def add_arguments(self, parser):
        parser.add_argument("ruta", nargs="?", default="data/museos.xlsx")

    def handle(self, *args, **options):
        ruta = Path(options["ruta"])
        if not ruta.exists():
            raise CommandError(f"No existe el archivo: {ruta}")
        hoja = load_workbook(ruta, read_only=True, data_only=True).active
        filas = hoja.iter_rows(values_only=True)
        encabezados = next(filas, None)
        if not encabezados:
            raise CommandError("El Excel no contiene encabezados.")
        creados = actualizados = 0

        for fila in filas:
            d = dict(zip(encabezados, fila))
            nombre = str(d.get("Museo_en_la_lista") or "").strip()
            if not nombre:
                continue
            direccion = str(d.get("Dirección") or "").strip()
            if "SIN REGISTRO" in direccion.upper():
                direccion = ""
            valor_libre = str(d.get("Entrada_libre") or "").strip().lower()
            libre = valor_libre in ("sí", "si", "yes", "true", "1")
            lat = self.numero(d.get("Latitud"))
            lon = self.numero(d.get("Longitud"))
            defaults = {
                "direccion": direccion,
                "horario_evento": str(d.get("Horario_Noche_de_los_Museos_2026") or "").strip(),
                "entrada_libre": libre,
                "gratuidad_confirmada": libre,
                "latitud": lat, "longitud": lon,
                "tipo_lugar": str(d.get("Tipo_de_lugar") or "").strip(),
                "municipio": str(d.get("Municipio") or "").strip(),
                "fuente": str(d.get("Fuente_de_la_información") or "").strip(),
                "registro_fuente": str(d.get("Fila_en_CSV") or "").strip(),
            }
            museo, creado = Museo.objects.get_or_create(nombre=nombre, defaults=defaults)
            if creado:
                creados += 1
            else:
                # Completa datos ausentes; no sobrescribe información ya cargada con celdas vacías.
                for campo, valor in defaults.items():
                    actual = getattr(museo, campo)
                    if valor not in ("", None) and (actual in ("", None) or (campo in ("entrada_libre", "gratuidad_confirmada") and valor)):
                        setattr(museo, campo, valor)
                museo.save()
                actualizados += 1

        self.stdout.write(self.style.SUCCESS(
            f"Importación terminada. Nuevos: {creados}; revisados/actualizados: {actualizados}; total: {Museo.objects.count()}."
        ))

    @staticmethod
    def numero(valor):
        try:
            return float(valor) if valor not in (None, "") else None
        except (TypeError, ValueError):
            return None
