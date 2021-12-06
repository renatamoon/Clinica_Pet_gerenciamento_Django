from django.shortcuts import render, redirect
from ..forms import pet_forms
from ..entidades import pet
from ..services import pet_service, cliente_service, consulta_service
from django.contrib.auth.decorators import login_required


@login_required()
def inserir_pet(request, id):
    if request.method == "POST":
        form_pet = pet_forms.PetForm(request.POST)
        proprietario = cliente_service.listar_cliente_id(id)
        if form_pet.is_valid():
            nome = form_pet.cleaned_data["nome"]
            idade = form_pet.cleaned_data["idade"]
            categoria = form_pet.cleaned_data["categoria"]
            cor = form_pet.cleaned_data["cor"]
            peso = form_pet.cleaned_data["peso"]
            raca = form_pet.cleaned_data["raca"]
            genero = form_pet.cleaned_data["genero"]
            pet_novo = pet.Pet(proprietario=proprietario, 
                                nome=nome, 
                                idade=idade, 
                                categoria=categoria, 
                                cor=cor, peso=peso, 
                                raca=raca, 
                                genero=genero)
            pet_service.cadastrar_pet(pet_novo) #cadastrar no banco de dados
            return redirect('listar_clientes')
    else:
        form_pet = pet_forms.PetForm()
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})


@login_required()
def listar_pet_id(request, id):
    pet = pet_service.listar_pet_id(id)
    consultas = consulta_service.listar_consultas(id)
    return render(request, 'pets/lista_pet.html', {'pet': pet, 'consultas': consultas})


@login_required()
def editar_pet(request, id):
    pet_antigo = pet_service.listar_pet_id(id)
    form_pet = pet_forms.PetForm(request.POST or None, instance=pet_antigo)
    if form_pet.is_valid():
        proprietario = form_pet.cleaned_data["proprietario"]
        nome = form_pet.cleaned_data["nome"]
        idade = form_pet.cleaned_data["idade"]
        categoria = form_pet.cleaned_data["categoria"]
        cor = form_pet.cleaned_data["cor"]        
        pet_novo = pet.Pet(proprietario=proprietario, nome=nome, idade=idade, cor=cor, categoria=categoria)
        pet_service.editar_pet(pet_antigo, pet_novo)
        return redirect('listar_pets')
    return render(request, 'pets/form_pet.html', {'form_pet': form_pet})


def listar_pets(request):
    pets = pet_service.listar_pets_all()
    return render(request, 'pets/listar_pets.html', {'pets':pets})