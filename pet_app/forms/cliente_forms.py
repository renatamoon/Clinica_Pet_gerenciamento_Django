from django import forms
from ..models import Cliente

#criando o forms do cliente com tudo o que será renderizado dentro do formulário

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento', 'cpf', 'profissao']