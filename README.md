<h1 align="center">People ID</h1>

<p align="center" >
  <img alt="print do projeto" width="400" src="https://github.com/LucasdsGomes/Django-CRUD/assets/114450172/96d2aeb2-37cc-430e-a75b-c720d00849fa">
</p>

---

Neste projeto você encontrará um aplicativo que tem como o intuito ser um sistema para gerenciamento de funcionarios de 
uma empresa, atualmente ele apenas faz o gerenciamento de funcionario, mas calma que ele ainda só está començando. 
As próximas features serão o incremento dos dados das pessoas com novas informações e gerenciamento de setores e seus 
funcionarios, se tiver mais algum ideias de feature para implementarmos crie uma issue ou me envia no 
[linkedin](https://www.linkedin.com/in/lucasdsgomes/).

O projeto está sendo desenvolvido em Django, um framework de desenvolvimento web em Python. O intuito desse projeto é ser um modelo
ideal para iniciantes que desejam aprender o básico do Django e sua integração com HTML usando Bootstrap e CSS.

---

## Tecnologias:

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

---

## Funcionalidades:

- Gerencimento de funcionarios.
- Autenticação (em andamento).
- Gerenciamento de setores de uma empresa (em andamento).
- Visualização da tabela de folga de um setor (em andamento).

---

## Configuração do Ambiente

### Instalação das dependencias:

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas em sua máquina:

- Python

Faça o clone deste repositório em sua máquina local usando o seguinte comando:

```bash
git clone https://github.com/seu-usuario/crud-django-bootstrap.git
```
      
Navegue até o diretório do projeto:

```bash
cd crud-django-bootstrap
```

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:

  ```bash
  venv\Scripts\activate
  ```

- No macOS e Linux:

  ```bash
  source venv/bin/activate
  ```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Preparação do banco de dados:

Execute as migrações do Django para criar as tabelas do banco de dados:

```bash
python manage.py migrate
```

Inicialização do servidor Django em desenvolvimento:

```bash
python manage.py runserver
```

---  

## Acesso ao sistema:

Abra o navegador e visite o endereço http://localhost:8000 para ver o projeto em ação.

## Contribuindo

Se você deseja contribuir com melhorias ou correções, fique à vontade para abrir uma pull request explicando as mudanças propostas. Será um prazer contar com sua colaboração!
