from django.shortcuts import redirect, render

from pet_app.models import Cliente

from ..forms.cliente_forms import ClienteForm
from ..forms.endereco_forms import EnderecoClienteForm
from ..entidades import cliente, endereco
from ..services import cliente_service, endereco_service


def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    #todos os clientes cadastrados no banco de dados
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})



def cadastrar_cliente(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoClienteForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data["nome"]
            email = form_cliente.cleaned_data["email"]
            cpf = form_cliente.cleaned_data["cpf"]
            data_nascimento = form_cliente.cleaned_data["data_nascimento"]
            profissao = form_cliente.cleaned_data["profissao"]
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = endereco_service.cadastrar_endereco(endereco_novo)
                cliente_novo = cliente.Cliente(nome=nome, email=email, data_nascimento=data_nascimento,
                                           profissao=profissao, cpf=cpf, endereco=endereco_bd)
                cliente_service.cadastrar_cliente(cliente_novo)
                return redirect('listar_clientes')
    else:
        form_cliente = ClienteForm()
        form_endereco = EnderecoClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})


# def editar_cliente(request, id):
#     cliente = Cliente.objects.get(id=id)
#     form_cliente = ClienteForm(request.POST or None, instance=cliente)
#     if form_cliente.is_valid():
#         form_cliente.save()
#         return redirect('listar_clientes')
#     return render(request, 'clientes/form_cliente.html', {'form_cliente': form_cliente})


def remover_cliente_db(cliente):
    cliente.delete()


def remover_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form_cliente = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        remover_cliente_db(cliente)
        return redirect('listar_cliente')
    return render(request, 'clientes/confirma_exclusao.html', {'form_cliente': form_cliente})
