from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistroForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UsuarioPersonalizado

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def get_data(request):
    print(request.user.nombre)
    return render(request, 'tu_template.html', {
        'user': request.user
    })

def inicio(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            print("Intentando autenticar:", username)  # DEBUG
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                print("Autenticación fallida")  # DEBUG
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales incorrectas'})
        else:
            print("Formulario inválido")  # DEBUG
            return render(request, 'login.html', {'form': form, 'error': 'Formulario inválido'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'Inicio.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
        
         # Toma el usuario y contraseña del formulario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Autenticar y loguear al usuario recién creado
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página principal

    else:
        form = UserCreationForm()

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