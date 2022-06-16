<div align="center">
  <h1>PsiPerfil</h1>

  <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">

  <h2>Menu</h2>
  <p>
    :small_orange_diamond:<a href="#introducao">Introdução</a>
    :small_orange_diamond:<a href="#tecnologias">Tecnologias</a>
    :small_orange_diamond:<a href="#backlog">Backlog</a>
    :small_orange_diamond:<a href="#comousar">Como usar</a>
  </p>
</div>

<a name="introducao"></a>
## :dart: Introdução

O Psiperfil é um projeto que faz o gerenciamento de preenchimento de formulários psicológicos. 
O desafio principal foi adapta-lo às normas da LGPD, implementando um sistema de "Opt-in and Opt-out", 
onde o usuário pode fazer o gerenciamento dos dados que ele deseja permitir que sejam guardados pela 
aplicação.

<div align="center">
  <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
</div>

## :rocket: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Postgres](https://www.postgresql.org/)

## :white_check_mark: Backlog

- O Usuário deve ser capaz de responder os formulários;
- O usuário deve ser capaz de atualizar seus dados pessoais;
- O usuário deve ser capaz de gerenciar suas informações pessoais;
- O usuário deve ser capaz de criar, editar e excluir seu cadastro.

<div align="center">
  <img src="https://github.com/felipemessi/psiperfil/blob/main/.github/LGPD.jpg">
</div>

## 🔖 Como usar

Para utilizar basta que você tenha o Python e o Postgres instalado.

Basta executar os seguintes comandos:

```python
pip install poetry
poetry init
poetry install
```

Depois, crie um arquivo "local_settings.py" dentro da pasta psiperfil e coloque adapte o script a seguir:

```python
# local_settings.py
import os
from pathlib import Path

from .settings import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your_secret_key"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# Configure aqui sua conexão com o postgres ou mantenha assim para utilizar o sqlite3
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # ou sua conexão Postgres
        'NAME': os.path.join(BASE_DIR, 'psiperfil.sqlite3'),
    }
}
```

por fim, execute

```python
poetry start
```

<div align="center">
  <img src="https://github.com/felipemessi/psiperfil/blob/main/.github/api_psiperfil.png">
</div>


## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---

Feito com ♥ by felipemessi :wave:
