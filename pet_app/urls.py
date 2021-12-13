from django.urls import path
from .views import cliente_views, pet_views, consulta_views, funcionario_views, autenticacao_views, dashboard_views

urlpatterns = [
    #----------------------urls de clientes
    path    ('cadastrar_cliente',           cliente_views.cadastrar_cliente,            name='cadastrar_cliente'),
    path    ('listar_clientes',             cliente_views.listar_clientes,              name='listar_clientes'),
    path    ('listar_cliente/<int:id>',     cliente_views.listar_cliente_id,            name='listar_cliente'),
    path    ('remover_cliente/<int:id>',    cliente_views.remover_cliente,              name='remover_cliente'), 
    path    ('editar_cliente/<int:id>',     cliente_views.editar_cliente,               name='editar_cliente'),
    
    #-----------------------urls de pets
    path    ('cadastrar_pet/<int:id>',      pet_views.inserir_pet,                      name='cadastrar_pet'),
    path    ('listar_pet/<int:id>',         pet_views.listar_pet_id,                    name='listar_pet_id'),
    path    ('listar_pets',                 pet_views.listar_pets,                      name='listar_pets'),

    #-----------------------urls de consultas
    path    ('cadastrar_consulta/<int:id>', consulta_views.inserir_consulta,            name='cadastrar_consulta'),
    path    ('lista_consulta/<int:id>',     consulta_views.listar_consulta_id,          name='listar_consulta_id'),
    
    #-----------------------urls de funcionarios
    path    ('cadastrar_funcionario',       funcionario_views.inserir_funcionario,      name='cadastrar_funcionario'),
    path    ('listar_funcionarios',         funcionario_views.listar_funcionarios,      name='listar_funcionarios'),
    path    ('login',                       autenticacao_views.login_usuario,           name='login'),
    path    ('logout',                      autenticacao_views.deslogar_usuario,        name='logout'),
    path    ('dashboard',                   dashboard_views.dashboard,                  name='dashboard'),        
]