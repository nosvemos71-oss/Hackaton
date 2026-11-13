# Museos gratis hoy — Bogotá

MVP para encontrar museos en Bogotá con entrada gratuita confirmada para hoy y abrir la ruta en Google Maps.

> La necesidad está planteada como hipótesis hasta contrastarla con posibles visitantes.

## Objetivo del producto
Ayudar a personas en Bogotá a encontrar museos que puedan visitar gratis hoy, consultar información útil y saber cómo llegar.

## Alcance del MVP
- Consultar el conjunto oficial [Mapa de Espacios de las Artes, las Culturas y los Saberes](https://www.datos.gov.co/Cultura/Mapa-de-Espacios-de-las-Artes-las-Culturas-y-los-S/p9n3-av9n).
- Filtrar exclusivamente municipio Bogotá, D.C. y lugares cuyo tipo sea museo. Mostrar nombre, dirección y coordenadas cuando estén disponibles.
- Confirmar gratuidad y horario de hoy en fuentes oficiales de cada museo. El dataset ubica espacios; no confirma por sí solo precios ni horarios. Mostrar fecha y fuente de verificación y marcar con claridad lo no confirmado.
- Abrir Google Maps para llegar al museo elegido usando sus coordenadas.
- Manejar errores de consulta, resultados vacíos y campos faltantes.

## Sprint 1 — Hackathon
**Sprint Goal:** una persona puede consultar museos de Bogotá, distinguir cuáles tienen gratuidad confirmada hoy y abrir su ruta en Google Maps. Es una iteración de una sesión; seleccionar solo trabajo viable durante las tres horas de desarrollo.

## Definition of Done
- Django inicia y el flujo principal funciona en navegador.
- Se usan datos reales, el filtro corresponde solo a Bogotá y la fuente queda atribuida.
- Precio y horario de hoy están confirmados con fuente oficial y fecha, o se muestran como pendientes.
- Los casos de error, datos incompletos y cero resultados tienen respuesta comprensible.
- Los criterios de aceptación y una comprobación funcional real están registrados.
- El README describe los pasos de instalación y ejecución verificados.
- El cambio está revisado e integrado; Project e Issues reflejan el estado real.

## Plan de trabajo
- [#2 Filtrar museos de Bogotá desde datos abiertos](https://github.com/nosvemos71-oss/Hackaton/issues/2)
- [#3 Verificar gratuidad y horarios vigentes para hoy](https://github.com/nosvemos71-oss/Hackaton/issues/3)
- [#4 Abrir ruta del museo seleccionado en Google Maps](https://github.com/nosvemos71-oss/Hackaton/issues/4)
- [#5 Documentar producto, DoD y pasos reproducibles](https://github.com/nosvemos71-oss/Hackaton/issues/5)
- Product Goal, Sprint Goal y DoD están en el README del Project.

## Reparto sugerido
1. Datos: API de datos.gov.co, filtro Bogotá y manejo de errores.
2. Investigación: verificación de gratuidad y horarios en fuentes oficiales.
3. Interfaz: vistas y plantillas Django.
4. Integración/calidad: enlace a Google Maps, README, comprobaciones y demo.

El equipo debe asignar las personas en el Project y asegurar que todas comprendan el recorrido.

## Estado técnico
El repositorio está en planificación y todavía no contiene el starter Django. Completen aquí dependencias e instrucciones de ejecución después de implementar y verificar el proyecto; no registren pruebas que no hayan corrido.

## Demo y retrospectiva
Mostrar problema/hipótesis y beneficiario, fuente y limitaciones, Sprint Goal, recorrido implementado, DoD cumplida y pendientes. Anotar qué funcionó, principal obstáculo y una acción concreta de mejora.
