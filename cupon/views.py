from django.shortcuts import render, redirect
from .forms import CuponForm
from django.contrib import messages
from .models import Cupon

def registro(request):
    if request.method == 'POST':
        form = CuponForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cupón registrado correctamente')
            return redirect('registro_cupon')  # Redirige a la página de login
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            
    else:
        form = CuponForm()

    return render(request, 'registro_cupon.html', {'form': form})


def listar_cupones(request):
    cupones = Cupon.objects.all()
    
    context = {
        'cupones': cupones
    }
    return render(request, 'lista_cupones.html', context)