from django.db import models

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(unique=True)
    precio = models.PositiveIntegerField()
    oferta = models.BooleanField(default=False)
    cantidad = models.SmallIntegerField()
    imagen = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre_categoria = models.CharField(unique=True)
    descripcion = models.TextField(blank=True)
    ultima_modificacion = models.DateField(auto_now=False, auto_now_add=False)
    reabastecer = models.BooleanField()

    producto = models.ForeignKey(
        Platos,
        on_delete=models.PROTECT, related_name="platos"
    )

    def __str__(self):
        return self.nombre_categoria