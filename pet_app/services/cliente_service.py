from ..models import cliente_models

def cadastrar_cliente(cliente):    
    cliente_models.Cliente.objects.create( nome=cliente.nome, 
                            email=cliente.email, 
                            endereco=cliente.endereco, 
                            cpf=cliente.cpf,
                            data_nascimento=cliente.data_nascimento, 
                            profissao=cliente.profissao)


def listar_clientes():
    return cliente_models.Cliente.objects.all()   


def listar_cliente_id(id):
    return cliente_models.Cliente.objects.get(id=id)


def editar_cliente(cliente, cliente_novo):
    cliente.nome                =           cliente_novo.nome
    cliente.email               =           cliente_novo.email
    cliente.endereco            =           cliente_novo.endereco
    cliente.cpf                 =           cliente_novo.cpf
    cliente.data_nascimento     =           cliente_novo.data_nascimento
    cliente.profissao           =           cliente_novo.profissao
    cliente.save(force_update=True)


def remover_cliente(cliente):
    cliente.delete()
