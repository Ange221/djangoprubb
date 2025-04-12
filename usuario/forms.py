from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import AuthenticationForm
from .models import UsuarioPersonalizado
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )


    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("password")
        return cleaned_data

    def save(self, commit=True):
        # Guardar la contraseña de forma encriptada
        usuario = super().save(commit=False)
        usuario.set_contrasena(self.cleaned_data["password"])
        
        if commit:
            usuario.save()
        return usuario
