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


@login_required(login_url='login')
def get_data(request):
    print(request.user.nombre)
    return render(request, 'tu_template.html', {
        'user': request.user
    })

@login_required(login_url='login')
def inicio(request):
    return render(request, 'index.html')

def login_view(request):
    print("1")
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            print("Intentando autenticar:", username)  # DEBUG
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.rol == 'cliente':
                    return redirect('historial_compra')  # Reemplaza con tu ruta real
                else:
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
    print(request.user.is_superuser)
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print("✅ Formulario válido")
            user = form.save(commit=False)
            if request.user.is_authenticated:
                user.rol = form.cleaned_data["rol"]
            else:
                user.rol = "cliente"
            user.save()
            messages.success(request, "Usuario registrado correctamente.")

            if request.user.is_superuser:
                return redirect('lista_usuarios')

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            if user is not None and not request.user.is_superuser:
                login(request, user)
                return redirect('historial_compra')
            else:
                
                print("❌ Falló autenticación")
        else:
            print("❌ Errores del formulario:", form.errors)
            return render(request, 'registrousuario.html', {'form': form, 'error': form.errors})
    else:
        form = RegistroForm()
    return render(request, 'registrousuario.html', {'form': form})

@login_required(login_url='login')
def listar_usuarios(request):
    empleados = UsuarioPersonalizado.objects.filter(rol='empleado')
    clientes = UsuarioPersonalizado.objects.filter(rol='cliente')
    
    context = {
        'empleados': empleados,
        'clientes': clientes,
    }
    return render(request, 'lista_usuarios.html', context)

@login_required(login_url='login')
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


