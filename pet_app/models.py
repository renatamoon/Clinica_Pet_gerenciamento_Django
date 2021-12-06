from django.db import models
from django.db.models import enums
from django.db.models.deletion import CASCADE
from django_localflavor_br.br_states import  STATE_CHOICES
from django.contrib.auth.models import AbstractUser

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

    # def clean(self):  
    #     error_messages = {}      
    #     nome_pet_enviado = self.nome or None
    #     nome_pet_salvo = None

    #     pet = Pet.objects.filter(nome=nome_pet_enviado).first()
        
    #     if pet:
    #         nome_pet_salvo = pet.nome

    #         if nome_pet_salvo is not None and self.id != pet.id:
    #             error_messages['nome'] = 'Nome do Pet já existe'


    # class Meta:
    #     constraints = [models.UniqueConstraint(name='my_pet_unique_constraint', fields = ['nome', 'proprietario'])]   
    

class ConsultaPet(models.Model):
    DOUTOR_CHOICES = (
        ('Ma', 'Maria Lima'),
        ('Fc', 'Fernanda Cardoso Lira'),
        ('Af', 'Amanda Finamor'),
        ('Vm', 'Victoria Misson'),
        ('As', 'Amanda dos Santos Silva'),
        ('Cv', 'Cássia Vasconcellos'),
        ('Rp', 'Regina Elis Pascoal'),
    )

    ESPECIALIDADES_CHOICES = (
        ('Cg', 'Clinico Geral'),
        ('Cd', 'Cardiologia'),
        ('De', 'Dermatologia'),
        ('Fi', 'Fisioterapia'),
        ('He', 'Hematologia'),
        ('Ne', 'Neurologia'),
        ('Or', 'Ortopedia'),
    )

    pet = models.ForeignKey(Pet, on_delete=CASCADE, null=False, blank=False)
    data = models.DateField(null=False, blank=False, auto_now_add=True)
    doutor = models.CharField(max_length=2, choices=DOUTOR_CHOICES, blank=True, null=True)
    motivo_consulta = models.CharField(max_length=200, null=False, blank=False)
    medicamento_atual = models.TextField(null=False, blank=False)
    medicamentos_prescritos = models.TextField(null=False, blank=False)
    exames = models.TextField(null=False, blank=False)
    especialidade = models.CharField(max_length=2, choices=ESPECIALIDADES_CHOICES, blank=True, null=True)     
    observacoes = models.TextField(null=False, blank=False)


class Funcionario(AbstractUser):
    #faz com que a classe funcionario tbem possua os campos de autenticacao de usuario
    CARGO_CHOICES = [
        (1, 'Médico Veterinario'),
        (2, 'Financeiro'),
        (3, 'Atendimento'),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    nascimento = models.DateField()
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False)