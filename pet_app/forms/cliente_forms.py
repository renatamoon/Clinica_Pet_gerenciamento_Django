from django import forms
from django.forms import widgets, DateInput
from ..models import cliente_models

#criando o forms do cliente com tudo o que será renderizado dentro do formulário

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente_models.Cliente
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': "date"}
            )
        }
        