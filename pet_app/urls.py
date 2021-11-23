from django.urls import path
from .views import cliente_views

urlpatterns = [
    path('cadastrar_cliente', cliente_views.cadastrar_cliente, name='cadastrar_cliente' ),
    path('lista_clientes', cliente_views.listar_clientes, name='listar_cliente' ),
    path('lista_cliente/<int:id>', cliente_views.listar_cliente_id, name='listar_cliente_id' ),      

]