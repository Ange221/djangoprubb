from django.urls import path
from . import views

urlpatterns = [
    path('cupon/', views.registro, name='registro_cupon'),  
    path('listar_cupones/', views.listar_cupones, name='listar_cupones'),  # Vista de registro
    #path('editar/', views.listar_, name='Editar_usuarios')
]
