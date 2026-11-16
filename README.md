# Museos gratis hoy en Bogotá

Aplicación web académica con Django, SQLite, Leaflet, OpenStreetMap y OSRM.

## Qué incluye
- Listado de museos importados desde `data/museos.xlsx`.
- Búsqueda por nombre/dirección y filtros por entrada libre/no confirmada.
- Mapa interactivo OpenStreetMap con marcadores.
- Selección de 2 a 10 museos y orden sugerido de visita mediante OSRM.
- Distinción explícita entre entrada libre indicada en el Excel y gratuidad no confirmada.
- Zona horaria `America/Bogota`.

## Requisitos
- Python 3.10 o superior.
- Conexión a Internet para cargar Leaflet, teselas de OpenStreetMap y calcular rutas con OSRM.

## Instalación en Windows (PowerShell)
```powershell
cd museos_bogota_completo
py -m venv venv
.env\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py importar_museos
python manage.py runserver
```
Abre http://127.0.0.1:8000/

## Instalación en macOS/Linux
```bash
cd museos_bogota_completo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py importar_museos
python manage.py runserver
```

## Panel administrativo
```bash
python manage.py createsuperuser
```
Luego abre http://127.0.0.1:8000/admin/

## Cómo funciona el recorrido
1. Marca al menos dos museos que tengan coordenadas.
2. Pulsa **Calcular mejor recorrido**.
3. El navegador envía las coordenadas a OSRM en formato longitud,latitud.
4. OSRM devuelve el orden optimizado y la geometría de la ruta.
5. Leaflet dibuja el recorrido sobre OpenStreetMap.

El MVP calcula un recorrido de automóvil abierto (sin regresar al punto inicial), limitado a 10 museos por consulta. No es una predicción de tráfico en vivo ni una optimización de horarios de visita. El servicio público de demostración OSRM puede tener límites o indisponibilidad.

## Decisiones y límites de los datos
- `Entrada_libre = Sí` se muestra como **Entrada libre según Excel 2026**, no como gratuidad vigente hoy.
- Las celdas vacías de entrada libre se muestran como **Gratuidad no confirmada**.
- Los horarios son los del evento Noche de los Museos 2026; no se presentan como horarios habituales.
- No se inventan direcciones ni coordenadas faltantes.
- Algunos registros de origen tienen coordenadas muy próximas o repetidas. El mapa usa exactamente las coordenadas suministradas; por eso algunos marcadores pueden quedar superpuestos.
- El Excel contiene registros duplicados por fuente/tipo de lugar. La importación consolida por nombre para evitar repetir un museo en la lista.

## Fuentes
- Excel proporcionado: `data/museos.xlsx`.
- OpenStreetMap: https://www.openstreetmap.org/
- Leaflet: https://leafletjs.com/
- OSRM: https://project-osrm.org/
- Historias de usuario del proyecto: archivo `Historias_de_Usuario_Museos_Gratis_Bogota.docx`.

## Antes de publicar
Configura `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` y `DJANGO_ALLOWED_HOSTS`. Para producción, usa un proveedor de rutas/tiles con condiciones de uso apropiadas y revisa su capacidad, cuota y atribución.
