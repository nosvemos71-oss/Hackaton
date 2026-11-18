# Museos gratis hoy en Bogotá

Aplicación web académica desarrollada con Django que permite consultar museos y lugares culturales de Bogotá, buscar información, identificar los registros con entrada libre indicada y planificar recorridos mediante un mapa interactivo.

## 1. Descripción del proyecto

El proyecto busca facilitar el acceso a información sobre museos y espacios culturales de Bogotá mediante una aplicación web. La plataforma permite consultar los lugares registrados, buscar por nombre o dirección, revisar información disponible y visualizar su ubicación en un mapa.

También permite seleccionar varios museos para generar una ruta sugerida, facilitando la organización de recorridos culturales.

## 2. Problema identificado

Las personas interesadas en visitar museos y espacios culturales de Bogotá pueden tener dificultades para encontrar información organizada sobre su ubicación, horarios y condiciones de entrada.

La información puede encontrarse distribuida en diferentes páginas y fuentes, lo que dificulta comparar lugares y planificar una visita.

Por esta razón, se propone desarrollar una aplicación que reúna la información disponible y facilite su consulta.

## 3. Objetivo general

Desarrollar una aplicación web que permita consultar museos y espacios culturales de Bogotá, visualizar su información y ubicación geográfica, identificar los registros que indican entrada libre y facilitar la planificación de recorridos.

## 4. Beneficiarios

- Habitantes de Bogotá interesados en conocer espacios culturales.
- Turistas nacionales y extranjeros.
- Estudiantes y docentes.
- Personas que buscan actividades culturales y recorridos por la ciudad.

## 5. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Django:** framework para el desarrollo web.
- **SQLite:** sistema de gestión de base de datos utilizado en el proyecto.
- **HTML y CSS:** estructura y presentación de las páginas.
- **JavaScript:** funcionalidades e interactividad.
- **Leaflet:** biblioteca para mostrar mapas interactivos.
- **OpenStreetMap:** servicio de mapas y datos geográficos.
- **OSRM:** servicio utilizado para calcular rutas entre ubicaciones.

## 6. Funcionalidades principales

- Consultar el listado de museos y lugares culturales registrados.
- Buscar museos por nombre o dirección.
- Filtrar los registros que indican entrada libre.
- Consultar la información detallada de cada lugar.
- Visualizar la ubicación de los museos en un mapa interactivo.
- Seleccionar entre 2 y 10 museos para planificar un recorrido.
- Generar una ruta sugerida utilizando OSRM.
- Consultar la información disponible sobre direcciones y coordenadas.

## 7. Fuente de información y datos

El proyecto utiliza un archivo Excel ubicado en:

`data/museos.xlsx`

El archivo contiene información de museos y espacios culturales, incluyendo:

- Nombre del lugar.
- Tipo de lugar.
- Dirección.
- Municipio y departamento.
- Latitud y longitud.
- Información sobre entrada libre.
- Horarios asociados a la Noche de los Museos 2026.
- Fuente de información registrada para cada lugar.

En el archivo se identifican registros asociados a SIMCO y PULEP.

También se tuvo como referencia la información publicada sobre la Noche de los Museos 2026 en Bogotá:

https://bogota.gov.co/que-hacer/cultura/2026-11/planes-gratuitos-en-bogota-noche-de-los-museos-13-noviembre-2026

**Consideraciones sobre la fuente:** la aplicación importa los registros desde el archivo Excel incluido en el proyecto. En dicho archivo se identifican las referencias SIMCO y PULEP. La referencia a la publicación de Bogotá.gov.co sirve como contexto del evento. No se afirma que la aplicación consuma directamente una API de datos.gov.co, ya que el procedimiento documentado para cargar la información es mediante el archivo Excel.

## 8. Requisitos previos

Para ejecutar el proyecto se necesita:

- Python 3.10 o superior.
- pip.
- Git (opcional, para clonar el repositorio).
- Conexión a internet para visualizar los mapas y consultar el servicio de rutas.

## 9. Instalación y ejecución en Windows

### 9.1. Clonar el repositorio

```bash
git clone https://github.com/nosvemos71-oss/Hackaton.git
```

Ingresar a la carpeta:

```bash
cd Hackaton
```

### 9.2. Crear el entorno virtual

```bash
py -m venv venv
```

### 9.3. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.bat
```

### 9.4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 9.5. Aplicar las migraciones

```bash
python manage.py migrate
```

### 9.6. Importar los museos

```bash
python manage.py importar_museos
```

### 9.7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

`http://127.0.0.1:8000/`

## 10. Instalación y ejecución en macOS o Linux

Crear el entorno virtual:

```bash
python3 -m venv venv
```

Activarlo:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Aplicar las migraciones:

```bash
python manage.py migrate
```

Importar los museos:

```bash
python manage.py importar_museos
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

## 11. Panel de administración

Django permite administrar los registros desde su panel administrativo.

Para crear un superusuario:

```bash
python manage.py createsuperuser
```

Después de iniciar el servidor, ingresar a:

`http://127.0.0.1:8000/admin/`

Utilizar las credenciales creadas para ingresar.

## 12. Funcionamiento del mapa y las rutas

La aplicación utiliza Leaflet para visualizar los museos en un mapa interactivo y OpenStreetMap como fuente cartográfica.

Para generar un recorrido:

1. El usuario consulta los museos disponibles.
2. Selecciona entre 2 y 10 lugares.
3. La aplicación utiliza las coordenadas disponibles.
4. Se realiza una solicitud al servicio OSRM.
5. La ruta sugerida se representa en el mapa.

El servicio de rutas recibe las coordenadas en el orden longitud y latitud.

La ruta es una sugerencia basada en la información geográfica disponible. No representa una optimización de horarios, tráfico en tiempo real ni confirmación de que los lugares estén abiertos.

## 13. Consideraciones y limitaciones de los datos

Para evitar mostrar información incorrecta, se tienen en cuenta las siguientes condiciones:

- Los registros que indican entrada libre se presentan de acuerdo con el valor disponible en el Excel.
- Cuando no existe información sobre gratuidad, esta no debe interpretarse como entrada gratuita.
- Los horarios disponibles corresponden a la información asociada al evento Noche de los Museos 2026.
- No se deben inventar direcciones ni coordenadas cuando no estén disponibles.
- Algunos registros pueden presentar información incompleta.
- Pueden existir lugares repetidos o registros relacionados con diferentes tipos de espacios culturales.
- La información debe verificarse con fuentes oficiales antes de asegurar que un museo tiene entrada gratuita o está abierto en una fecha determinada.
- La aplicación depende de servicios externos para mostrar mapas y calcular recorridos.

## 14. Pruebas y verificación

Se realizaron pruebas automatizadas utilizando el módulo `TestCase` de Django para comprobar el funcionamiento de las principales funcionalidades de la aplicación.

### 14.1. Ejecución de las pruebas

Para ejecutar las pruebas de la aplicación se utilizó:

```bash
python manage.py test museos
```

### 14.2. Pruebas realizadas

Se implementaron 11 pruebas automatizadas:

| Prueba | Funcionalidad verificada |
|---|---|
| `test_pagina_principal_carga` | Comprueba que la página principal cargue correctamente y utilice la plantilla correspondiente. |
| `test_listado_de_museos` | Verifica que se muestren los museos registrados y que el total de resultados sea correcto. |
| `test_busqueda_por_nombre` | Comprueba la búsqueda de museos por nombre. |
| `test_busqueda_por_direccion` | Comprueba la búsqueda de museos por dirección. |
| `test_filtro_entrada_libre` | Verifica el filtro de registros con entrada libre. |
| `test_filtro_no_confirmado` | Comprueba el filtro de registros cuya entrada no está confirmada como gratuita. |
| `test_detalle_de_museo` | Verifica que se pueda consultar el detalle de un museo existente. |
| `test_mapa_recibe_museos_con_coordenadas` | Comprueba que los datos enviados al mapa incluyan los museos con coordenadas y sus valores de latitud y longitud. |
| `test_busqueda_sin_resultados` | Verifica que una búsqueda sin coincidencias no genere errores y devuelva cero resultados. |
| `test_museo_sin_coordenadas_no_genera_error` | Comprueba que un museo sin coordenadas no se incluya entre los puntos enviados al mapa. |
| `test_detalle_museo_inexistente` | Verifica que al consultar un museo que no existe se obtenga una respuesta 404. |

### 14.3. Resultado obtenido

Durante la ejecución se obtuvo el siguiente resultado:

```text
Found 11 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........
----------------------------------------------------------------------
Ran 11 tests in 1.771s

OK
Destroying test database for alias 'default'...
```

**Conclusión:** las 11 pruebas automatizadas finalizaron correctamente. Django no identificó problemas durante la comprobación del sistema y todas las pruebas obtuvieron el resultado `OK`.

### 14.4. Otros comandos de verificación

Verificar la configuración de Django:

```bash
python manage.py check
```

Verificar las migraciones:

```bash
python manage.py showmigrations
```

Las pruebas automatizadas comprueban el comportamiento de las vistas y los datos utilizados en los casos de prueba. También se debe realizar una revisión manual de la navegación, el mapa y la generación de rutas.

## 15. Organización del proyecto

La estructura principal del proyecto es:

```text
Hackaton/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── data/
│   └── museos.xlsx
│
├── museos/
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── importar_museos.py
│   ├── templates/
│   │   └── museos/
│   │       ├── detalle.html
│   │       └── lista.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## 16. Configuración para producción

Para ejecutar el proyecto en un entorno de producción se recomienda configurar las variables de entorno y no dejar información sensible directamente en el código.

Variables recomendadas:

```env
DJANGO_SECRET_KEY=tu_clave_secreta
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=tu-dominio.com
```

No se deben subir claves privadas ni contraseñas al repositorio.

---

# 17. Planeación Scrum

## 17.1. Product Goal

Ayudar a las personas en Bogotá a encontrar museos y espacios culturales, consultar cuáles tienen entrada gratuita confirmada para el día de la visita y acceder a información que facilite llegar a ellos.

El producto busca reunir la información disponible en una aplicación web sencilla, teniendo en cuenta que la gratuidad y los horarios deben verificarse mediante fuentes oficiales.

## 17.2. Sprint Goal

Lograr que una persona pueda consultar museos de Bogotá, reconocer cuáles tienen entrada gratuita confirmada para el día de la visita y acceder a una opción para consultar cómo llegar.

Para el desarrollo del Sprint se estableció una sesión de trabajo de aproximadamente tres horas. Por esta razón, se seleccionaron tareas pequeñas y prioritarias que pudieran trabajarse durante el tiempo disponible, manteniendo las demás actividades organizadas en el Product Backlog.

## 17.3. Product Backlog

El Product Backlog reúne las necesidades y actividades identificadas para construir y mejorar el producto.

Las tareas se relacionan con los Issues existentes en el repositorio de GitHub:

| Issue | Nombre de la tarea | Estado |
|---|---|---|
| #1 | Definir problema, usuario y alcance del MVP en Bogotá. | Cerrado |
| #2 | Filtrar museos de Bogotá desde datos abiertos | Cerrado |
| #3 | Verificar gratuidad y horarios vigentes para hoy | Cerrado |
| #4 | Abrir ruta del museo seleccionado en Google Maps | Cerrado |
| #5 | Documentar producto, DoD y pasos reproducibles | Cerrado |
| #7 | Creación visual de la base de datos | Cerrado |
| #8 | Creación de página funcional con Django | Cerrado |

### Descripción de las tareas

**Issue #1. Definir problema, usuario y alcance del MVP en Bogotá.**

Identificar el problema que se quiere solucionar, los usuarios beneficiarios y las funcionalidades principales que debe tener la primera versión del producto.

**Issue #2. Filtrar museos de Bogotá desde datos abiertos.**

Consultar y organizar los datos disponibles, filtrar los registros correspondientes a Bogotá D. C. y mostrar información como nombre, dirección, coordenadas y fuente de los datos.

**Issue #3. Verificar gratuidad y horarios vigentes para hoy.**

La necesidad identificada consiste en consultar fuentes oficiales para comprobar si los museos tienen entrada gratuita y están abiertos en la fecha de consulta. Cuando no exista confirmación, la información debe mostrarse como pendiente o no confirmada.

**Issue #4. Abrir ruta del museo seleccionado en Google Maps.**

La necesidad identificada consiste en permitir que el usuario consulte cómo llegar al museo seleccionado mediante Google Maps, siempre que existan coordenadas disponibles.

**Issue #5. Documentar producto, DoD y pasos reproducibles.**

Documentar el objetivo del producto, el objetivo del Sprint, el Product Backlog, el Sprint Backlog, la Definition of Done y las instrucciones para instalar y ejecutar el proyecto.

**Issue #7. Creación visual de la base de datos.**

Organizar la estructura de la base de datos y definir cómo se almacenará la información de los museos.

**Issue #8. Creación de página funcional con Django.**

Desarrollar la aplicación web utilizando Django, integrando la información de los museos y las funcionalidades principales de consulta.

## 17.4. Sprint Backlog

El Sprint Backlog contiene las tareas seleccionadas para el Sprint, junto con el trabajo necesario para cumplir el Sprint Goal.

En el tablero GitHub Projects del equipo, al momento de actualizar esta documentación, se registró la siguiente distribución:

| Columna del tablero | Cantidad de elementos |
|---|---:|
| Pendientes | 0 |
| En progreso | 0 |
| En revisión | 0 |
| Hecho | 5 |
| Finalizar | 2 |
| **Total** | **7** |

Los siete elementos se encuentran cerrados en GitHub. El tablero conserva cinco elementos en la columna Hecho y dos en Finalizar.

La distribución anterior refleja las cantidades observadas en el tablero y no asigna nombres de tareas a cada columna sin comprobar su correspondencia individual.

Para hacer seguimiento al trabajo se utilizaron:

- Tareas registradas como Issues.
- Responsables asignados en GitHub.
- Estados de seguimiento en GitHub Projects.
- Evidencias de implementación y pruebas.

## 17.5. Definition of Done (DoD)

Una tarea se considera terminada cuando cumple las condiciones necesarias para garantizar que funciona y que puede integrarse correctamente al proyecto.

Se establecieron los siguientes criterios:

- El proyecto Django inicia sin errores que impidan su funcionamiento.
- El flujo principal de navegación funciona en el navegador.
- La información utilizada tiene una fuente identificada y sus limitaciones están documentadas.
- Los registros de Bogotá D. C. se identifican correctamente.
- La gratuidad y los horarios solo se presentan como confirmados cuando existe una fuente oficial y una fecha de verificación.
- Se manejan errores de consulta, datos faltantes y búsquedas sin resultados.
- Los criterios de aceptación de cada tarea se comprueban.
- Se ejecutan pruebas funcionales y se registran sus resultados reales.
- El README contiene los pasos necesarios para instalar y ejecutar el proyecto.
- Los cambios se revisan antes de integrarse a la rama principal.
- Los Issues y el GitHub Project reflejan el estado real del trabajo.

## 18. Trabajo colaborativo con GitHub

El repositorio utilizado para el desarrollo del proyecto es:

https://github.com/nosvemos71-oss/Hackaton

GitHub se utilizó para organizar las actividades, registrar los cambios del código y realizar el seguimiento del trabajo del equipo.

### 18.1. Issues

Se crearon siete Issues para identificar las tareas del proyecto, describir su propósito y establecer criterios de aceptación.

Al momento de actualizar esta documentación, los siete Issues (#1, #2, #3, #4, #5, #7 y #8) aparecen cerrados en GitHub.

### 18.2. Pull Requests

Durante el desarrollo se registraron los siguientes Pull Requests:

| PR | Nombre | Estado |
|---|---|---|
| #6 | docs: add Bogota museums MVP plan | Abierto |
| #9 | Archivo_excel_museos_actualizado | Cerrado sin fusionar |
| #10 | Actualización y corrección del sistema de museos | Fusionado |

El PR #6 corresponde a la documentación de la planeación del producto y está relacionado con el Issue #5.

El PR #9 corresponde a una actualización del archivo Excel utilizado como fuente de información. Se encuentra cerrado, pero no fusionado.

El PR #10 contiene actualizaciones y correcciones del sistema de museos y aparece fusionado en el repositorio.

Los Pull Requests permiten presentar cambios para su revisión antes de integrarlos a la rama principal. El estado de cada uno se registra según lo que muestra GitHub. No se afirma que todos hayan recibido una aprobación formal de revisión.

### 18.3. Repositorio

Enlace al repositorio:

https://github.com/nosvemos71-oss/Hackaton

## 19. Retrospectiva

Durante el desarrollo del proyecto se trabajó en la identificación del problema, la organización de las tareas, la consulta de información, el desarrollo de la aplicación y la documentación.

Entre los aspectos importantes del trabajo se encuentran:

- La importancia de organizar las tareas antes de comenzar a programar.
- La necesidad de verificar la información antes de mostrarla al usuario.
- La utilidad de GitHub para distribuir actividades y llevar un registro de los cambios.
- La importancia de probar las funcionalidades antes de considerarlas terminadas.
- La necesidad de mantener actualizados el README, los Issues y el tablero del proyecto.

Como oportunidades de mejora se identifican la verificación de gratuidad y horarios con fuentes oficiales, la actualización de los datos y el fortalecimiento de las pruebas funcionales.

---

**Proyecto académico: Museos gratis hoy en Bogotá**

Desarrollado con Python y Django.
