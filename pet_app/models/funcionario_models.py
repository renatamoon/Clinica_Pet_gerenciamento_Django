from django.db import models
from django.contrib.auth.models import AbstractUser


#-------------------------funcionario models

class Funcionario(AbstractUser):
    #faz com que a classe funcionario tbem possua os campos de autenticacao de usuario
    CARGO_CHOICES = [
        (1, 'Médico Veterinario'),
        (2, 'Financeiro'),
        (3, 'Atendimento'),
    ]
    nome            =       models.CharField      (     max_length=50, null=False, blank=False              )
    nascimento      =       models.DateField      (     null=False, blank=False                             )
    cargo           =       models.IntegerField   (     choices=CARGO_CHOICES, null=False, blank=False      )