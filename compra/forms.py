from .models import Compra
from django import forms

class CompraForm(forms.ModelForm):
    cupon_codigo = forms.CharField(
        required=False,  # Hazlo opcional
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Código de Cupón'})
    )
    
    class Meta:
        model = Compra
        fields = ['email', 'descripcion', 'litros_vendidos', 'total_venta', 'metodo_pago']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['litros_vendidos'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['total_venta'].widget.attrs.update({'class': 'form-control form-control-user'})
        self.fields['metodo_pago'].widget.attrs.update({'class': 'form-control'})


class CorreoForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-user'})
    
    email = forms.EmailField(max_length=255)