from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Museo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=200)),
                ("direccion", models.CharField(blank=True, max_length=250)),
                ("horario_evento", models.CharField(blank=True, max_length=120, verbose_name="Horario Noche de los Museos 2026")),
                ("entrada_libre", models.BooleanField(default=False)),
                ("gratuidad_confirmada", models.BooleanField(default=False)),
                ("latitud", models.FloatField(blank=True, null=True)),
                ("longitud", models.FloatField(blank=True, null=True)),
                ("tipo_lugar", models.CharField(blank=True, max_length=100)),
                ("municipio", models.CharField(blank=True, max_length=100)),
                ("fuente", models.CharField(blank=True, max_length=100)),
                ("registro_fuente", models.CharField(blank=True, max_length=30)),
            ],
            options={"ordering": ["nombre"]},
        ),
        migrations.AddConstraint(
            model_name="museo",
            constraint=models.UniqueConstraint(fields=("nombre",), name="unique_museo_nombre"),
        ),
    ]
