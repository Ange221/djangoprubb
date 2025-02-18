from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import LoginForm, RegistroForm
from django.contrib import messages
from .models import UsuarioPersonalizado

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')  # Redirige a la página principal
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'index.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('registro')  # Redirige a la página de login
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})


def listar_usuarios(request):
    empleados = UsuarioPersonalizado.objects.filter(rol='empleado')
    clientes = UsuarioPersonalizado.objects.filter(rol='cliente')
    
    context = {
        'empleados': empleados,
        'clientes': clientes,
    }
    return render(request, 'lista_usuarios.html', context)

def eliminar_usuario(request, usuario_id):
    # Asegurarse de que el usuario tenga permisos para eliminar
    if not request.user.is_staff:  # Solo los administradores pueden eliminar
        messages.error(request, "No tienes permisos para eliminar este usuario.")
        return redirect('lista_usuarios')  # Redirigir a la página del perfil si no tiene permisos

    # Obtener el usuario que se desea eliminar
    usuario = get_object_or_404(UsuarioPersonalizado, id=usuario_id)

    # Eliminar el usuario
    usuario.delete()

    # Mostrar mensaje de éxito
    messages.success(request, "El usuario ha sido eliminado correctamente.")
    
    return redirect('lista_usuarios')  # Redirige a la lista de usuarios u otra página relevante