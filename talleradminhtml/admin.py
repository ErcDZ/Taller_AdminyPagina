from django.contrib import admin
from .models import Platos, Categoria

# Register your models here.
class PlatoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "oferta", "imagen"]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nombre_categoria", "ultima_modificacion", "reabastecer"]
    
admin.site.register(Platos)
admin.site.register(Categoria)