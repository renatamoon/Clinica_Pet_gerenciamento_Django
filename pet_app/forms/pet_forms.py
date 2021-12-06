from django import forms
from ..models import Pet

#forms de endereco

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['nome', 'idade', 'peso', 'categoria', 'cor', 'raca', 'genero']
        exclude = ['proprietario'] #nao validar a info    

