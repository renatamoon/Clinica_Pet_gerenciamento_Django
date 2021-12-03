from django.shortcuts import render, redirect
from ..forms import pet_forms
from ..entidades import pet
from ..services import pet_service, cliente_service

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
            pet_novo = pet.Pet(proprietario=proprietario, nome=nome, idade=idade, categoria=categoria, cor=cor, peso=peso, raca=raca, genero=genero)
            pet_service.cadastrar_pet(pet_novo)
            return redirect('listar_clientes')
            