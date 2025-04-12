from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),  # Vista de login
    path('registro/', views.registro, name='registro'),  # Vista de registro
    path('get/', views.get_data, name='data'),
    path('lista_usuarios/', views.listar_usuarios, name='lista_usuarios'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
     path('registroCliente/', views.registro, name='registro'),  # Vista de registro

]
