from django.shortcuts import render, redirect
from .forms import CompraForm, CorreoForm
from django.contrib import messages
from .models import Compra, UsuarioCupon
from .utils.aceptacion_cupon import get_cupon
from cupon.models import Cupon
from usuario.models import UsuarioPersonalizado

def registro(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            cupon_codigo = form.cleaned_data.get('cupon_codigo')
            total_venta = compra.total_venta  # Inicializar total_venta con el valor de la compra
            
            if cupon_codigo:
                # Procesar el código de cupón
                print(f"Código de cupón ingresado: {cupon_codigo}")
                
                # Buscar el cupón en UsuarioCupon y verificar si es válido
                cupon = UsuarioCupon.objects.filter(cupon__nombre=cupon_codigo, is_valid=False).first()
                
                if cupon:
                    # Si hay un cupón válido, aplicar el descuento
                    total_venta -= cupon.cupon.descuento
                    compra.cupon = cupon_codigo
                    cupon.is_valid = True  # Marcar como usado
                    cupon.save()
                    messages.success(request, 'Tuvo un descuento en la venta')
                else:
                    # Si el cupón no es válido
                    messages.error(request, 'El cupón ha sido usado o está mal escrito')
                    return redirect('registro_compra')
            
            compra.total_venta = total_venta  # Actualizar el total con el descuento
            compra.save()

            # Verificar si el usuario tiene un cupon disponible
            result = get_cupon(form.cleaned_data['email'])
            if result:
                messages.success(request, 'Compra registrada correctamente, usuario con cupón disponible')
            else:
                messages.success(request, 'Compra registrada correctamente')

            return redirect('registro_compra')  # Redirige a la página correspondiente

        else:
            # Manejo de errores en el formulario
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            
    else:
        form = CompraForm()

    return render(request, 'registro_compra.html', {'form': form})


def listar_compras(request):
    compras = Compra.objects.all()
    
    context = {
        'compras': compras
    }
    return render(request, 'lista_compras.html', context)


def listar_compras_usuario(request):
    if request.method == 'POST':
        form = CorreoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            compras = Compra.objects.filter(email=email)
            cupones = UsuarioCupon.objects.filter(email=email)
            return render(request, 'historial_compra.html', {'compras':compras,'cupones':cupones})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = CorreoForm()

    return render(request, 'historial_compra.html', {'form': form})


def historial_compra(request, id):
    compra = Compra.objects.get(id=id)
    cupon = compra.cupon
    cupon = Cupon.objects.filter(nombre=cupon).first()
    total = 0
    if cupon:
        total = compra.total_venta + cupon.descuento
    else:
        total = compra.total_venta
    usuario = UsuarioPersonalizado.objects.filter(email=compra.email).first()
    return render(request, 'compra_cupon.html', {'compra': compra,'cupon':cupon,'usuario':usuario, 'total':total})





