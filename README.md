# Clinica_Pet_gerenciamento_Django
<i>Sistema de Gestão de Clínica PET</i>

<p align="center">
  <a href="#projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Como Executar o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#imagens">Imagens do Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#links_apps">Links Úteis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
 
</p>

## <a id="projeto"> 💻 SOBRE ESTE PROJETO </a>

Projeto a fim de criar um Sistema de Gerenciamento de Clínica PET, para ser cadastrado Clientes,
Pets, Consultas dos Pets, Funcionários e Usuários a fim de permitir o acesso ao sistema.

Algumas funcionalidades:

    *CRUD de Clientes;
    *CRUD de Funcionarios;
    *CRUD de Usuários;
    *CRUD de Pets e Consultas;
    *Print da página do extrato da consulta;
    *Envio por e-mail dos dados da consulta;

🟩 Status do projeto: EM ANDAMENTO ... <br>

<hr>
  
  ## <a id="tecnologias"> 🧪 TECNOLOGIAS UTILIZADAS NESTE PROJETO </a>

Front-End:

![HTML 5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

Desenvolvimento da parte de Administração:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Bower version](https://img.shields.io/bower/v/adminlte.svg)

Banco de Dados:

![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

Desenvolvido no:

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

<hr>

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a> 

*No Windows

<b>-Clone o repositório com o camando:</b> `git clone https://github.com/renatamoon/Clinica_Pet_gerenciamento_Django.git` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: Caso ocorra um erro na ativação:</b> entre no powershell e digite o seguinte comando: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>-Execução do arquivo requirements: </b>`pip install -r requirements.txt`<br>

*No Linux:

<b>-Baixe o repositorio<br>
<b>-Criando virtual environment:</b> `virtualenv venv`<br>
<b>-Ativando o virtual environment:</b> `. venv/bin/activate`<br>
<b>-Execução do arquivo requirements e instalar dependencias:</b> `pip install -r requirements.txt`<br>
  
 <hr> 
  
*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'host_bd',
        'PORT': 'porta_bd',
        'NAME': 'pet_app',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'    
    }
}
```
 *Migre o banco de dados com: `python manage.py migrate` <br>
 *Execute o servidor: `python manage.py runserver` <br>
  
<hr>

## <a id="imagens"> 🔴 IMAGENS: </a> 
<br>
-Tela de clientes cadastrados na clínica:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/145451834-d6e8391b-2b42-4449-83d1-8c65af0225fa.png)
<br>
<br>
-Formulário de cadastro de Clientes:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/145452401-21d0db80-e29c-4b37-87e7-bc7fd217a7b0.png)
<br>
<br>
-Tela com a listagem de pets cadastrados:
<br>
<br>  
![image](https://user-images.githubusercontent.com/87100340/145452461-e4a51748-77c9-489e-a698-6998348dab52.png)
br>
<br>  
-Perfil do cliente listando seus dados, os pets cadastrados em nome dele e consultas de todos os pets cadastrados:
 <br>
<br>
![image](https://user-images.githubusercontent.com/87100340/145452556-3debd028-0ce5-45ba-978e-11f9f9229872.png)
<br>
<br>
-Perfil do Pet cadastrado naquele usuário:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/145453080-24462c66-0d61-4f1a-b132-23d3f06f5160.png)
<br>
<br> 
-Extrato do formulário com todas as infos das consultas:
<br>
<br> 
![image](https://user-images.githubusercontent.com/87100340/145452701-6c07b478-61f5-45e9-81d5-4e7a754d88bd.png)
<br>
<br>
-Extrato do formulário com todas as infos das consultas:
<br>
<br>
![image](https://user-images.githubusercontent.com/87100340/145452898-3ae5a416-cc30-46da-975b-afba07ade254.png)
<br>
<br>
-Funcionários cadastrados na clínica onde os mesmos tem seus acessos conforme informado nas views e com certas permissões:
<br>
<br>  
![image](https://user-images.githubusercontent.com/87100340/145452832-f1c2a4a0-5389-4a33-b11b-af0a2d27aed6.png)  
<br>
<br>
-DASHBOARD da clínica em construção (ainda estático) apenas aguardando o módulo de pagamentos que será integrado em breve.
<br>
<br>    
![image](https://user-images.githubusercontent.com/87100340/145453617-fda3eb31-4055-4794-9ade-7aab5eb3134a.png)

<hr>
  
## <a id="links_apps"> 🔴 LINKS ÚTEIS </a> 

*USANDO O ADMINLTE3 - Bootstrap Admin Dashboard Template<br>
<br>
https://adminlte.io/<br>  

*VALIDADOR DE CPF - Essa é uma implementação simples e enxuta de validadores para CPF de usuários.
https://github.com/gabrielloliveira/django-cpf<br>
<br>

*CURSO DE DJANGO COM CHART.JS: https://www.youtube.com/watch?v=HozwGeEiXIk
<hr>
