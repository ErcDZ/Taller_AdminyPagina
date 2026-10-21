from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.TextField(unique=True)
    precio = models.PositiveIntegerField()
    oferta = models.BooleanField(default=False)
    cantidad = models.SmallIntegerField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre_categoria = models.TextField(unique=True)
    descripcion = models.CharField(blank=True)
    ultima_modificacion = models.DateField(auto_now=False, auto_now_add=False)
    reabastecer = models.BooleanField()

    producto = models.ForeignKey(
        Platos,
        on_delete=models.PROTECT, related_name="platos"
    )

    def __str__(self):
        return self.nombre_categoria