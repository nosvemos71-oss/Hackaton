from django.contrib import admin
from .models import Museo

@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "entrada_libre", "direccion", "municipio", "fuente")
    list_filter = ("entrada_libre", "municipio", "fuente")
    search_fields = ("nombre", "direccion")
