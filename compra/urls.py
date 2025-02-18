from django.urls import path
from . import views

urlpatterns = [
    path('compra/', views.registro, name='registro_compra'),  # Página principal
    path('listar_compras/', views.listar_compras, name='listar_compras'),  # Vista de login
    path('historial_compra/', views.listar_compras_usuario, name='historial_compra'),  # Vista de registro
    path('compra_cupones/<int:id>/', views.historial_compra, name='compra_cupones'),  # Vista de registro
    #path('editar/', views.listar_, name='Editar_usuarios')
]
