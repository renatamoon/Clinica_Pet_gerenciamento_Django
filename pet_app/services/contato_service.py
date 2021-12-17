from ..models import contato_models



def cadastrar_contatos(contato):
    contato_models.Contato.objects.create(  nome_completo=contato.nome_completo, 
                                            email=contato.email, 
                                            telefone=contato.telefone, 
                                            mensagem=contato.mensagem    )
    


def listar_contatos():
    contatos = contato_models.Contato.objects.all()
    return contatos





