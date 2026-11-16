from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250, blank=True)
    horario_evento = models.CharField("Horario Noche de los Museos 2026", max_length=120, blank=True)
    entrada_libre = models.BooleanField(default=False)
    gratuidad_confirmada = models.BooleanField(default=False)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    tipo_lugar = models.CharField(max_length=100, blank=True)
    municipio = models.CharField(max_length=100, blank=True)
    fuente = models.CharField(max_length=100, blank=True)
    registro_fuente = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ["nombre"]
        constraints = [
            models.UniqueConstraint(fields=["nombre"], name="unique_museo_nombre")
        ]

    def __str__(self):
        return self.nombre

    @property
    def tiene_coordenadas(self):
        return self.latitud is not None and self.longitud is not None
