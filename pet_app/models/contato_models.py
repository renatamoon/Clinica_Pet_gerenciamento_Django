from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator


#models de Contato da Página Index - formulário para recepção de contatos

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Contato(TimeStampedModel): 
    nome_completo            =       models.CharField    (   max_length=100, null=False, blank=False )
    email                    =       models.EmailField   (   null=False, blank=False )    
    phoneNumberRegex         =       RegexValidator      (   regex = r"^\+?1?\d{8,15}$")
    phoneNumber              =       models.CharField    (   validators = [phoneNumberRegex], max_length = 16, unique = True)   
    mensagem                 =       models.TextField    (   max_length=25, null= False, blank=False )

    def __str__(self):
        return self.nome_completo

#-------------------------------------------------------------------obs:
#https://www.delftstack.com/pt/howto/django/django-phone-number-field/
# O validador phoneNumberRegex valida o valor inserido para o CharField. 
# Novamente, os números de telefone são armazenados no formato E.164.