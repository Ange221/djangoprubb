from .models import Cupon
from django import forms

class CuponForm(forms.ModelForm):
    class Meta:
        model = Cupon
        fields = ['nombre', 'descripcion', 'litros']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['litros'].widget.attrs.update({'class': 'form-control form-control-user'})