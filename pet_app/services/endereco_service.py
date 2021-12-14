from ..models import cliente_models

def cadastrar_endereco(endereco):
    return cliente_models.EnderecoCliente.objects.create(   rua=endereco.rua,
                                                            cidade=endereco.cidade,
                                                            estado=endereco.estado)


def listar_endereco_id(id):
    return cliente_models.EnderecoCliente.objects.get(id=id)


def editar_endereco(endereco_antigo, endereco_novo):
    endereco_antigo.rua         =       endereco_novo.rua
    endereco_antigo.cidade      =       endereco_novo.cidade
    endereco_antigo.estado      =       endereco_novo.estado
    endereco_antigo.save(force_update=True)
    return endereco_antigo


def remover_endereco(endereco):
    endereco.delete()
