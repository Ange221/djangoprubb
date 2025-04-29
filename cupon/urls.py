from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pagina_empleado/', views.pagina_empleado, name='pagina_empleado'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('cupon/', views.registro, name='registro_cupon'),  
    path('listar_cupones/', views.listar_cupones, name='listar_cupones'),  # Vista de registro
    #path('editar/', views.listar_, name='Editar_usuarios')
]
