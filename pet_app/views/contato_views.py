from django.shortcuts import render
from pet_app.forms.contato_forms import ContatoForm
from ..models import contato_models



def listar_contatos(request):
    contatos = contato_models.Contato.objects.all()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})


def cadastrar_contato(request):
    form_contato = ContatoForm()
    return render(request, 'empresa/contato.html', {'form_contato': form_contato})
