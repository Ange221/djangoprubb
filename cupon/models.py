from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class Cupon(models.Model):
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    litros = models.IntegerField(unique=True)
    descuento = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre}"