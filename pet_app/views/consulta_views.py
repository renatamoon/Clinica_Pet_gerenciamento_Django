from ..forms import consulta_forms
from ..services import pet_service, consulta_service
from django.shortcuts import render, redirect
from ..entidades import consulta


def inserir_consulta(request, id):
    if request.method == "POST":
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.listar_pet_id(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data["motivo_consulta"]
            medicamento_atual = form_consulta.cleaned_data["medicamento_atual"]
            medicamentos_prescritos = form_consulta.cleaned_data["medicamentos_prescritos"]
            exames = form_consulta.cleaned_data["exames"]
            especialidade = form_consulta.cleaned_data["especialidade"]
            doutor = form_consulta.cleaned_data["doutor"]
            observacoes = form_consulta.cleaned_data["observacoes"]
            consulta_nova = consulta.ConsultaPet(pet=pet, 
                                                motivo_consulta=motivo_consulta, 
                                                medicamento_atual=medicamento_atual,
                                                medicamentos_prescritos=medicamentos_prescritos, 
                                                exames=exames, 
                                                especialidade=especialidade, 
                                                doutor=doutor,
                                                observacoes=observacoes)
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('listar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})


def listar_consulta_id(request, id):
    consulta = consulta_service.listar_consulta(id)
    return render(request, 'consultas/lista_consulta.html', {'consulta': consulta})