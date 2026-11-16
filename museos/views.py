from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Museo

def lista_museos(request):
    museos = Museo.objects.all()
    termino = request.GET.get("q", "").strip()
    filtro = request.GET.get("estado", "todos")
    if termino:
        museos = museos.filter(Q(nombre__icontains=termino) | Q(direccion__icontains=termino))
    if filtro == "gratis":
        museos = museos.filter(entrada_libre=True)
    elif filtro == "no_confirmado":
        museos = museos.filter(entrada_libre=False)

    puntos = []
    for m in museos:
        if m.tiene_coordenadas:
            puntos.append({
                "id": m.id, "nombre": m.nombre, "direccion": m.direccion,
                "lat": m.latitud, "lon": m.longitud,
                "gratis": m.entrada_libre, "horario": m.horario_evento,
                "fuente": m.fuente,
            })
    import json
    return render(request, "museos/lista.html", {
        "museos": museos, "puntos_json": json.dumps(puntos, ensure_ascii=False),
        "termino": termino, "filtro": filtro, "total": museos.count(),
        "total_gratis": Museo.objects.filter(entrada_libre=True).count(),
        "total_sin_confirmar": Museo.objects.filter(entrada_libre=False).count(),
    })

def detalle_museo(request, museo_id):
    museo = get_object_or_404(Museo, pk=museo_id)
    return render(request, "museos/detalle.html", {"museo": museo})
