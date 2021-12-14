from django import forms
from ..models import consulta_models


class ConsultaPetForm(forms.ModelForm):
    class Meta:
        model = consulta_models.ConsultaPet
        fields = '__all__'
        exclude = ['pet', 'data']