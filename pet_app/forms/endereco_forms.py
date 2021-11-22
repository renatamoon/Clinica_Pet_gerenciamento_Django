from django import forms
from ..models import EnderecoCliente

#forms de endereco

class EnderecoClienteForm(forms.ModelForm):
    class Meta:
        model = EnderecoCliente
        fields = ['rua', 'cidade', 'estado']