from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    nome_da_empresa = "CLINICA PET"
    descricao_da_empresa = "A nossa rede de clínicas está no mercado a mais de 20 anos. São mais de 50 profissionais trabalhando conosco."

    contato_empresa = {
        "endereco": "Avenida Brigadeiro Faria Lima, 1987 - Itaim Bibi - São Paulo - SP",
        "telefone": "+55 11 97674-1514",
        "email": "clinicapet@clinicasp.com.br",
    }

    cursos_home = {
        "1": {"titulo": "Nossos Serviços", "descricao": "Nossos serviços de clínica vão desde de hemogramas, atendimento especializado com nosso melhores médicos veterinários, atendimento psicológico, fisioterapia integrada, espaço pet para o seu bichinho quando estiver nas nossas dependências."},
        "2": {"titulo": "Espaço Pet", "descricao": "O Espaço Pet, uma área exclusiva para cães e gatos, está ganhando cada vez mais destaque nos condomínios residenciais paulistanos. ... Essas áreas dedicadas aos animaizinhos contam com nomes variados, podendo ser chamadas."},
        "3": {"titulo": "Vacinação", "descricao": "Proteger o seu pet contra doenças infecciosas. Vaciná-lo irá permitir que ele permaneça saudável! Proteger as pessoas contra os agentes circulantes dessas doenças. A vacinação previne o contágio de um animal para o outro, ou mesmo para as pessoas."},

    }
    return render(request, 'empresa/index.html', {'nome_da_empresa': nome_da_empresa, 'descricao_da_empresa': descricao_da_empresa, 'contato_empresa': contato_empresa, 'cursos_home':cursos_home})



def sobre(request):
    nome_da_empresa = "CLINICA PET"
    descricao_da_empresa = "A nossa rede de clínicas está no mercado a mais de 20 anos. São mais de 50 profissionais trabalhando conosco."

    contato_empresa = {
        "endereco": "Avenida Brigadeiro Faria Lima, 1987 - Itaim Bibi - São Paulo - SP",
        "telefone": "+55 11 97674-1514",
        "email": "clinicapet@clinicasp.com.br",
        }
    return render(request, 'empresa/about.html', {'nome_da_empresa': nome_da_empresa, 'descricao_da_empresa': descricao_da_empresa, 'contato_empresa': contato_empresa})


def servicos(request):
    return HttpResponse("Página de Serviços")