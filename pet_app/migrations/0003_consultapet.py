# Generated by Django 3.2.9 on 2021-12-05 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0002_pet_created_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaPet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('doutor', models.CharField(blank=True, choices=[('Ma', 'Maria Lima'), ('Fc', 'Fernanda Cardoso Lira'), ('Af', 'Amanda Finamor'), ('Vm', 'Victoria Misson'), ('As', 'Amanda dos Santos Silva'), ('Cv', 'Cássia Vasconcellos'), ('Rp', 'Regina Elis Pascoal')], max_length=2, null=True)),
                ('motivo_consulta', models.CharField(max_length=200)),
                ('medicamento_atual', models.TextField()),
                ('medicamentos_prescritos', models.TextField()),
                ('exames', models.TextField()),
                ('especialidade', models.CharField(blank=True, choices=[('Cg', 'Clinico Geral'), ('Cd', 'Cardiologia'), ('De', 'Dermatologia'), ('Fi', 'Fisioterapia'), ('He', 'Hematologia'), ('Ne', 'Neurologia'), ('Or', 'Ortopedia')], max_length=2, null=True)),
                ('observacoes', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_app.pet')),
            ],
        ),
    ]
