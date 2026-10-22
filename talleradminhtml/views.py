from django.shortcuts import render, get_object_or_404
from .models import Platos, Categoria

#todos los registros de la tabla
Platos.objects.all()

#solo si cumplen cierta condicion

Platos.objects.filter(disponible=True)
Platos.objects.filter(categoria__nombre='Postre')

#uno solo, o 404 si no existe
get_object_or_404(Platos, id=3)

# Create your views here.
def inicio(request):
    platos = Platos.objects.select_related("categoria") \
    .filter(disponible=True)

    contexto = {
        'platos': platos,
        'categorias': Categoria.objects.all()
    }

    return render (request, 'catalogo/inicio.html', contexto)