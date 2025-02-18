from django.db import models

# Create your models here.
class Cupon(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    litros = models.IntegerField(unique=True)
    descuento = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre}"