from django.db import models
from django.db.models.deletion import CASCADE


#models de Contato da Página Index - formulário para recepção de contatos

class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class Contato(TimeStampedModel): 
    nome_completo            =       models.CharField    (   max_length=100, null=False, blank=False, verbose_name='Nome' )
    email                    =       models.EmailField   (   null=False, blank=False, verbose_name='Insira seu e-mail' )
    telefone                 =       models.CharField    (   max_length=16, null=False, blank=False, verbose_name='Insira seu telefone'  )   
    mensagem                 =       models.TextField    (   max_length=300, null= False, blank=False, verbose_name='Deixe sua mensagem ...' )

    
#-------------------------------------------------------------------obs:
#https://www.delftstack.com/pt/howto/django/django-phone-number-field/
# O validador phoneNumberRegex valida o valor inserido para o CharField. 
# Novamente, os números de telefone são armazenados no formato E.164.