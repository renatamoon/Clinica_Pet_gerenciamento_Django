from django import forms
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm

from ..models import Funcionario


class FuncionarioForm(UserCreationForm):
    #UserCreationForm - faz todas as validações de senha e user
    class Meta:
        model = Funcionario
        fields = UserCreationForm.Meta.fields + ('nome', 'nascimento', 'cargo',)
        #cria os campos de user name e password e os campos que passamos
        widgets = {
            'nascimento': DateInput(
                attrs={'type': "date"}
            )
        }