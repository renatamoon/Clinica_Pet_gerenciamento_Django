from django import forms
from ..models import pet_models

#forms de endereco

class PetForm(forms.ModelForm):
    class Meta:
        model = pet_models.Pet
        fields = ['nome', 'idade', 'peso', 'categoria', 'cor', 'raca', 'genero']
        exclude = ['proprietario'] #nao validar a info    

