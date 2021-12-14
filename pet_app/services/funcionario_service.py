from ..models import funcionario_models


def listar_funcionarios():
    funcionarios = funcionario_models.Funcionario.objects.all()
    return funcionarios


def cadastrar_funcionario(funcionario):
    funcionario_models.Funcionario.objects.create(  nome=funcionario.nome, 
                                                    nascimento=funcionario.nascimento,
                                                    cargo=funcionario.cargo, 
                                                    username=funcionario.username, 
                                                    password=funcionario.password)