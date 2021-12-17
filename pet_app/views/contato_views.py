from django.shortcuts import render, redirect
from ..entidades import contato
from ..forms import contato_forms
from pet_app.forms.contato_forms import ContatoForm
from ..models import contato_models
from ..services import contato_service
from django.contrib import messages


def listar_contatos(request):
    contatos = contato_service.listar_contatos()
    return render(request, 'contatos/lista_contatos.html', {'contatos': contatos})



def cadastrar_contato(request):
    if request.method       ==      "POST":
        form_contato = ContatoForm(request.POST)
        if form_contato.is_valid():
            nome_completo = form_contato.cleaned_data['nome_completo']
            email = form_contato.cleaned_data['email']
            telefone = form_contato.cleaned_data['telefone']
            mensagem = form_contato.cleaned_data['mensagem']
            contato_novo = contato.Contato(  nome_completo=nome_completo,
                                                    email=email,
                                                    telefone=telefone,
                                                    mensagem=mensagem)
            contato_service.cadastrar_contatos(contato_novo)
            messages.success(request, 'Obrigada por enviar a mensagem. Retornaremos o mais rápido possível!')
            return redirect('cadastrar_contatos')
        else:
            # invalid form, print problems to terminal
            print(form_contato.errors)                                       
    else:
        form_contato = ContatoForm()
    return render(request, 'empresa/contato.html', {'form_contato': form_contato})


# def listar_cliente_id(request, id):
#     contato         =       contato_service.listar_contato_id(id)  
#     return render(request, 'contato/lista_contato_id.html', {'contato': contato})