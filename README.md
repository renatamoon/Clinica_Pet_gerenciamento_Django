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
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![MaterialUi](https://img.shields.io/badge/Material%20UI-007FFF?style=for-the-badge&logo=mui&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![JavaScript](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

Desenvolvimento da parte de Administração:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

Banco de Dados:

![Sqlite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
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
  
### Imagens do Sistema da Clínica: <br>
  
-Tela de Login da Clínica - acessível através do WebSite:<br><br>
![image](https://user-images.githubusercontent.com/87100340/147599710-af375aef-c7c0-4dd7-8fb2-af777482f28c.png)
<br>
-Tela de clientes cadastrados na clínica:<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456158-80ad12f2-8049-45d5-a409-d899cfb1f9c1.png)
<br><br>
-Tela de Cadastro do Cliente:<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456795-82fbb790-b016-4a09-a9cd-247ee0c8ff55.png)
<br><br>
-Tela com a listagem de pets cadastrados:<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456212-2d5c9e63-a3fa-47e0-a1a3-d20a76f99b00.png)
<br><br>
-Perfil do cliente listando seus dados, os pets cadastrados em nome dele e consultas de todos os pets cadastrados:<br>  
![image](https://user-images.githubusercontent.com/87100340/145456320-91190927-1ac3-40bd-b935-355c35bb92ae.png)
<br><br>
-Extrato do formulário com todas as infos das consultas:<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456372-652f9c2a-4696-45ce-a83f-e0305e06c9fa.png)
<br><br>
-Lista de Funcionários cadastrados na clínica:<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456266-f7bc5aad-358f-4930-9035-4051efac0e3f.png)
<br><br>
-Perfil do pet com todos os seus dados (por id) e também as consultas realizadas por este pet:
<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456440-e3586279-1cea-4264-8b7a-abb56e7d3ebf.png)
<br><br>
-DASHBOARD da clínica em construção (ainda estático) apenas aguardando o módulo de pagamentos que será integrado em breve:
<br><br>
![image](https://user-images.githubusercontent.com/87100340/145456551-61791d57-a679-4223-b03d-3eaf0b476499.png)
<br><br>
-Lista de Contatos recebidos (referente à página de formulário de contatos da Clínica - Website):
<br><br>
![image](https://user-images.githubusercontent.com/87100340/147599401-9cd6e564-243e-4d75-b2f6-47d92346b159.png)
<br><br>
-Extrato do contato recebido com as informações:
<br><br>
![image](https://user-images.githubusercontent.com/87100340/147599488-8c174e0e-7300-4aee-b0b6-63e657661b60.png)
<br>
  
### Imagens do Sistema do WebSite da Clínica:<br>

-Front Page - Navbar + Header da página<br><br>
![image](https://user-images.githubusercontent.com/87100340/147599881-19ca8efd-f139-4017-bc8b-a1653488876f.png)
<br><br>
-Cards de Planos de Saúde para Pets<br><br>  
![image](https://user-images.githubusercontent.com/87100340/147599925-1137a78f-8e08-4345-8dba-4b98998868a9.png)
<br><br>
-Cards de avaliação de clientes + Footer:<br><br>  
![image](https://user-images.githubusercontent.com/87100340/147599999-771cff5a-96fc-4dde-aa11-98108a93a1d6.png)
<br><br>
-Página Sobre a empresa:<br><br>
![image](https://user-images.githubusercontent.com/87100340/147600041-9604d256-8440-4804-8605-63e815d8cc3b.png)
<br><br>
-Página de Formulário de Contatos da empresa:<br><br>
![image](https://user-images.githubusercontent.com/87100340/147600070-3a7d4127-53c5-4463-92f6-7e811b9dcd08.png)
<br><br>

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
