from django.db import models
from django_localflavor_br.br_states import  STATE_CHOICES

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

#model do cliente - campos referente ao cliente no banco de dados

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES)
    #state choices foi importado para não precisar declarar manualmente7


class Cliente(TimeStampedModel):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE) #quando o usuario for removido, o endereço também
    #deve ser removido
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=True)
    data_nascimento = models.DateField(null=False, blank=False)
    profissao = models.CharField(max_length=25, null= False, blank=False)


class Pet(TimeStampedModel):
    CATEGORIA_PET_CHOICES = (
        ('Ca', 'Cachorro'),
        ('Ga', 'Gato'),
        ('Pa', 'Pássaro'),
        ('Ha', 'Hamister'),
    )

    COR_PET_CHOICES = (
        ('Pr', 'Preto'),
        ('Br', 'Branco'),
        ('Ci', 'Cinza'),
        ('Ma', 'Malhado'),
        ('Cr', 'Creme'),
        ('Mr', 'Marrom'),
        ('Am', 'Amarelo'),
    )

    GENERO_PET_CHOICES = (
        ('Fe', 'Femea'),
        ('Ma', 'Macho'),
    )

    nome = models.CharField(max_length=50, null=False, blank=False)
    idade = models.IntegerField(blank=False, null=False)
    peso = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_PET_CHOICES, blank=True, null=True)
    cor = models.CharField(max_length=2, choices=COR_PET_CHOICES, blank=True, null=True)
    raca = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=2, choices=GENERO_PET_CHOICES, blank=True, null=True)
    proprietario = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
