from django import forms
from ..models import cliente_models

#forms de endereco

class EnderecoClienteForm(forms.ModelForm):
    class Meta:
        model = cliente_models.EnderecoCliente
        fields = ['rua', 'cidade', 'estado']