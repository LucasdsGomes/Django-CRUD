# CRUD com Django
[Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-negative.png)

Bem-vindo ao repositório do CRUD com Django! Neste projeto, você encontrará um aplicativo CRUD (Create, Read, Update, Delete) desenvolvido em Django, um framework de desenvolvimento web em Python. Este projeto é ideal para iniciantes que desejam aprender o básico do Django e sua integração com HTML usando Bootstrap e CSS.

![image](https://github.com/LucasdsGomes/Django-CRUD/assets/114450172/96d2aeb2-37cc-430e-a75b-c720d00849fa)


# Funcionalidades
O CRUD com Django possui as seguintes funcionalidades:

Adicionar: Permite adicionar novos itens ao banco de dados.
Listar: Exibe uma lista de todos os itens existentes no banco de dados.
Detalhar: Mostra os detalhes de um item específico selecionado.
Editar: Permite a edição dos dados de um item existente.
Deletar: Remove um item do banco de dados permanentemente.
Configuração do Ambiente
Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas em sua máquina:

Python 
Django 
Bootstrap
CSS

# Instalação e Execução
Faça o clone deste repositório em sua máquina local usando o seguinte comando:
      git clone https://github.com/seu-usuario/crud-django-bootstrap.git
      
Navegue até o diretório do projeto:
  cd crud-django-bootstrap

Crie um ambiente virtual (recomendado) para isolar as dependências do projeto:
  python -m venv venv

Ative o ambiente virtual:
  No Windows:
  venv\Scripts\activate


  No macOS e Linux:
  source venv/bin/activate
Instale as dependências do projeto:

  pip install -r requirements.txt
Execute as migrações do Django para criar as tabelas do banco de dados:
  python manage.py migrate
  
Inicie o servidor de desenvolvimento do Django:
  python manage.py runserver

  
Abra o navegador e visite o endereço http://localhost:8000 para ver o projeto em ação.
Estrutura do Projeto
O projeto possui a seguinte estrutura de arquivos:

crud-django-bootstrap/
│
├── crud_app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   └── crud_app/
│   │       ├── index.html
│   │       ├── update.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── README.md

# Contribuindo
Se você deseja contribuir com melhorias ou correções, fique à vontade para abrir uma pull request explicando as mudanças propostas. Será um prazer contar com sua colaboração!
