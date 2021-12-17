from ..models import contato_models



def cadastrar_contatos(contato):
    contato_models.Contato.objects.create(  nome_completo=contato.nome_completo, 
                                            email=contato.email, 
                                            telefone=contato.telefone, 
                                            mensagem=contato.mensagem    )
    


def listar_contatos_all():
    return contato_models.Contato.objects.all()



def listar_contato_id(id):
    return contato_models.Contato.objects.get(id=id)
