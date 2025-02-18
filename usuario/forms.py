from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UsuarioPersonalizado

class LoginForm(AuthenticationForm):
    # Se añaden clases a los campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-user'})


class RegistroForm(forms.ModelForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'password', 'nombre', 'apellidos', 'rol', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['apellidos'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['rol'].widget.attrs.update({'class': 'form-control '})
        self.fields['contrasena_confirmacion'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user'})
    
    # Campo de la contraseña con confirmación
    contrasena_confirmacion = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("password")
        contrasena_confirmacion = cleaned_data.get("contrasena_confirmacion")

        if contrasena != contrasena_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data

    def save(self, commit=True):
        # Guardar la contraseña de forma encriptada
        usuario = super().save(commit=False)
        usuario.set_contrasena(self.cleaned_data["password"])
        
        if commit:
            usuario.save()
        return usuario
