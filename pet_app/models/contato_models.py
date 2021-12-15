from django.db import models
from django.db.models.deletion import CASCADE


#models de Contato da Página Index - formulário para recepção de contatos

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Cliente(TimeStampedModel):
    nome_completo            =       models.CharField    (   max_length=100, null=False, blank=False )
    email                    =       models.EmailField   (   null=False, blank=False )    
    telefone                 =       models.CharField    (   max_length=14, unique=True, null=False, blank=True  )    
    mensagem                 =       models.TextField    (   max_length=25, null= False, blank=False )