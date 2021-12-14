from django.db import models
from django.db.models.deletion import CASCADE
from ..models import cliente_models



class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


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

    nome            =          models.CharField     (    max_length=50, null=False, blank=False  )
    idade           =          models.IntegerField  (    blank=False, null=False )
    peso            =          models.CharField     (    max_length=50, null=False, blank=False  )
    categoria       =          models.CharField     (    max_length=2, choices=CATEGORIA_PET_CHOICES, blank=True, null=True  )
    cor             =          models.CharField     (    max_length=2, choices=COR_PET_CHOICES, blank=True, null=True    )
    raca            =          models.CharField     (    max_length=20, blank=True, null=True    )
    genero          =          models.CharField     (    max_length=2, choices=GENERO_PET_CHOICES, blank=True, null=True )
    proprietario    =          models.ForeignKey    (    cliente_models.Cliente, on_delete=models.CASCADE, blank=False, null=False  )


#-----------------------ainda em ajuste para que não haja pets duplicados
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
#------------------------------------------------------------------------   