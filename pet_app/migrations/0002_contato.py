# Generated by Django 3.2.9 on 2021-12-15 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('nome_completo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('mensagem', models.TextField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]