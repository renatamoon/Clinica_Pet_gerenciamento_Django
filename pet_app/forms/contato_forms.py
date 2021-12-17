from django import forms
from ..models import contato_models


class ContatoForm(forms.ModelForm):
    class Meta:
        model = contato_models.Contato
        fields = '__all__'
        widgets = {'telefone': forms.TextInput(attrs={'data-mask':"00-00000-0000"})}
