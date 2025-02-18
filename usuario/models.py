from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class UsuarioPersonalizado(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)
    ROL_CHOICES = [
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
    ]
    rol = models.CharField(max_length=10, choices=ROL_CHOICES)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.rol})"
    
    def set_contrasena(self, raw_contrasena):
        self.contrasena = make_password(raw_contrasena)
    
    def check_contrasena(self, raw_contrasena):
        return check_password(raw_contrasena, self.contrasena)