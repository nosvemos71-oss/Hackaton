
import json

from django.test import TestCase
from django.urls import reverse

from .models import Museo


class MuseoTests(TestCase):

    def setUp(self):
        self.museo1 = Museo.objects.create(
            nombre="Museo Nacional",
            direccion="Carrera 7, Bogotá",
            horario_evento="10:00 AM - 5:00 PM",
            entrada_libre=True,
            gratuidad_confirmada=True,
            latitud=4.6126,
            longitud=-74.0705,
            tipo_lugar="Museo",
            municipio="Bogotá",
            fuente="Prueba"
        )

        self.museo2 = Museo.objects.create(
            nombre="Museo del Oro",
            direccion="Parque Santander, Bogotá",
            entrada_libre=False,
            latitud=4.6018,
            longitud=-74.0722,
            tipo_lugar="Museo",
            municipio="Bogotá"
        )

        self.museo3 = Museo.objects.create(
            nombre="Museo Sin Coordenadas",
            direccion="Bogotá",
            entrada_libre=False
        )

    # 1. Página principal
    def test_pagina_principal_carga(self):
        response = self.client.get(reverse("lista_museos"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "museos/lista.html")

    # 2. Listado de museos
    def test_listado_de_museos(self):
        response = self.client.get(reverse("lista_museos"))

        self.assertContains(response, "Museo Nacional")
        self.assertContains(response, "Museo del Oro")
        self.assertEqual(response.context["total"], 3)

    # 3. Búsqueda por nombre
    def test_busqueda_por_nombre(self):
        response = self.client.get(
            reverse("lista_museos"),
            {"q": "Nacional"}
        )

        self.assertContains(response, "Museo Nacional")
        self.assertNotContains(response, "Museo del Oro")
        self.assertEqual(response.context["total"], 1)

    # Búsqueda por dirección
    def test_busqueda_por_direccion(self):
        response = self.client.get(
            reverse("lista_museos"),
            {"q": "Santander"}
        )

        self.assertContains(response, "Museo del Oro")
        self.assertEqual(response.context["total"], 1)

    # 4. Filtros
    def test_filtro_entrada_libre(self):
        response = self.client.get(
            reverse("lista_museos"),
            {"estado": "gratis"}
        )

        self.assertContains(response, "Museo Nacional")
        self.assertNotContains(response, "Museo del Oro")
        self.assertEqual(response.context["total"], 1)

    def test_filtro_no_confirmado(self):
        response = self.client.get(
            reverse("lista_museos"),
            {"estado": "no_confirmado"}
        )

        self.assertContains(response, "Museo del Oro")
        self.assertNotContains(response, "Museo Nacional")
        self.assertEqual(response.context["total"], 2)

    # 5. Detalle de un museo
    def test_detalle_de_museo(self):
        response = self.client.get(
            reverse("detalle_museo", args=[self.museo1.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "museos/detalle.html")
        self.assertContains(response, "Museo Nacional")

    # 6. Datos del mapa
    def test_mapa_recibe_museos_con_coordenadas(self):
        response = self.client.get(reverse("lista_museos"))

        puntos = json.loads(response.context["puntos_json"])

        self.assertEqual(len(puntos), 2)
        nombres = [punto["nombre"] for punto in puntos]
        
        self.assertIn("Museo Nacional", nombres)
        self.assertIn("Museo del Oro", nombres)
        
        for punto in puntos:
            self.assertIn("lat", punto)
            self.assertIn("lon", punto)

    # 7. Resultados vacíos
    def test_busqueda_sin_resultados(self):
        response = self.client.get(
            reverse("lista_museos"),
            {"q": "Museo Inexistente"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total"], 0)
        self.assertEqual(len(json.loads(
            response.context["puntos_json"]
        )), 0)

    # 8. Datos incompletos
    def test_museo_sin_coordenadas_no_genera_error(self):
        response = self.client.get(reverse("lista_museos"))

        self.assertEqual(response.status_code, 200)

        puntos = json.loads(response.context["puntos_json"])

        nombres = [punto["nombre"] for punto in puntos]

        self.assertNotIn("Museo Sin Coordenadas", nombres)

    def test_detalle_museo_inexistente(self):
        response = self.client.get(
            reverse("detalle_museo", args=[99999])
        )

        self.assertEqual(response.status_code, 404)
