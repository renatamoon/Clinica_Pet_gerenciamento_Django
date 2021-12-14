from ..models import consulta_models


def cadastrar_consulta(consulta):
    consulta_bd = consulta_models.ConsultaPet.objects.create(pet=consulta.pet, 
                                            motivo_consulta=consulta.motivo_consulta, 
                                            medicamento_atual=consulta.medicamento_atual, 
                                            medicamentos_prescritos=consulta.medicamentos_prescritos,
                                            exames=consulta.exames, 
                                            doutor=consulta.doutor,
                                            especialidade=consulta.especialidade,
                                            observacoes=consulta.observacoes)
    consulta_bd.save()

def listar_consultas(id):
    consultas = consulta_models.ConsultaPet.objects.filter(pet=id).all()
    return consultas

def listar_consultas_pets(id):
    consultas = consulta_models.ConsultaPet.objects.filter(pet__proprietario=id).all().order_by('-data')
    #tabela de pets e buscando o proprietario para verificar se o dono é igual ao id que estamos passando como parametro
    return consultas

def listar_consulta(id):
    consulta = consulta_models.ConsultaPet.objects.get(id=id)
    return consulta