from django.db import models
from django.db.models.deletion import CASCADE
from pet_app.models.pet_models import Pet



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

    pet                 =       models.ForeignKey   (   Pet, on_delete=CASCADE, null=False, blank=False     )
    data                =       models.DateField    (   null=False, blank=False, auto_now_add=True          )
    doutor              =       models.CharField    (   max_length=2, choices=DOUTOR_CHOICES, blank=True, null=True )
    motivo_consulta     =       models.CharField    (   max_length=200, null=False, blank=False )
    medicamento_atual   =       models.TextField    (   null=False, blank=False )
    medicamentos_prescritos =   models.TextField    (   null=False, blank=False )
    exames              =       models.TextField    (   null=False, blank=False )
    especialidade       =       models.CharField    (   max_length=2, choices=ESPECIALIDADES_CHOICES, blank=True, null=True )     
    observacoes         =       models.TextField    (   null=False, blank=False)