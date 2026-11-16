from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_museos, name="lista_museos"),
    path("museo/<int:museo_id>/", views.detalle_museo, name="detalle_museo"),
]
