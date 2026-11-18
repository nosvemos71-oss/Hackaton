
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from openpyxl import load_workbook

from museos.models import Museo


class Command(BaseCommand):
    help = "Importa museos desde data/museos.xlsx"

    def add_arguments(self, parser):
        parser.add_argument(
            "ruta",
            nargs="?",
            default="data/museos.xlsx"
        )

    def handle(self, *args, **options):
        ruta = Path(options["ruta"])

        if not ruta.exists():
            raise CommandError(
                f"No se encontró el archivo: {ruta}"
            )

        libro = load_workbook(
            ruta,
            read_only=True,
            data_only=True
        )

        hoja = libro["Museos"]

        filas = hoja.iter_rows(values_only=True)

        encabezados = next(filas, None)

        if not encabezados:
            raise CommandError(
                "El archivo Excel no contiene encabezados."
            )

        creados = 0
        actualizados = 0
        omitidos = 0

        for fila in filas:
            datos = dict(zip(encabezados, fila))

            nombre = str(
                datos.get("Nombre_en_la_lista") or ""
            ).strip()

            # Ignorar filas vacías y referencias.
            tipo_lugar = datos.get("Tipo_de_lugar")

            if not nombre or not tipo_lugar:
                omitidos += 1
                continue

            direccion = str(
                datos.get("Dirección") or ""
            ).strip()

            horario = str(
                datos.get("Horario") or ""
            ).strip()

            tipo_entrada = str(
                datos.get("Tipo_de_entrada") or ""
            ).strip()

            # Identificar entradas gratuitas.
            entrada_libre = tipo_entrada.lower().startswith(
                "gratuita"
            )

            latitud = self.convertir_numero(
                datos.get("Latitud")
            )

            longitud = self.convertir_numero(
                datos.get("Longitud")
            )

            defaults = {
                "direccion": direccion,
                "horario_evento": horario,
                "entrada_libre": entrada_libre,
                "gratuidad_confirmada": entrada_libre,
                "latitud": latitud,
                "longitud": longitud,
                "tipo_lugar": str(
                    tipo_lugar
                ).strip(),
                "municipio": str(
                    datos.get("Municipio") or ""
                ).strip(),
                "fuente": "Excel de museos de Bogotá",
                "registro_fuente": str(
                    datos.get("N°") or ""
                ).strip(),
            }

            museo, creado = Museo.objects.update_or_create(
                nombre=nombre,
                defaults=defaults
            )

            if creado:
                creados += 1
            else:
                actualizados += 1

        libro.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Importación terminada correctamente."
            )
        )

        self.stdout.write(
            f"Museos nuevos: {creados}"
        )

        self.stdout.write(
            f"Museos actualizados: {actualizados}"
        )

        self.stdout.write(
            f"Filas omitidas: {omitidos}"
        )

        self.stdout.write(
            f"Total de museos en la base de datos: "
            f"{Museo.objects.count()}"
        )

    @staticmethod
    def convertir_numero(valor):
        try:
            if valor is None or valor == "":
                return None

            return float(valor)

        except (TypeError, ValueError):
            return None
