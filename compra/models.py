from django.db import models
from datetime import date
from cupon.models import Cupon

# Create your models here.
class Compra(models.Model):
    COMPRA_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('credito', 'Credito'),
    ]

    email = models.EmailField(max_length=100)
    descripcion = models.CharField(max_length=100)
    litros_vendidos = models.IntegerField()
    total_venta = models.IntegerField()
    metodo_pago = models.CharField(max_length=10, choices=COMPRA_CHOICES)
    fecha_compra = models.DateField(default=date.today)
    cupon = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f"{self.descripcion}"


class UsuarioCupon(models.Model):
    email = models.EmailField()
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE)
    asignado_en = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(null=True, default=False)

