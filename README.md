
# Biblioteca Django :books:

## Requisitos:

1. Python 3.10.*


## Instalação(Windows):

1. Abra a pasta do projeto no terminal;

1. Execute o comando:  `python -m venv venv`;

1. Execute o comando:  `./venv/Scripts/activate`;

1. Execute o comando:  `pip install -r requirements.txt`;

1. Execute o comando: `python manage.py migrate`;

1. Execute o comando: `python manage.py loaddata seed.json`

1. Execute o comando: `python manage.py createsuperuser`; (Este comando cria um usuário administrador)

1. Execute o comando: `python manage.py runserver`;


## Instalação com docker:

1. Execute o comando `docker-compose up`

1. Execute o comando `docker-compose exec web python manage.py migrate`

1. Execute o comando `docker-compose exec web python manage.py loaddata seed.json`

1. Execute o comando `docker-compose exec web python manage.py createsuperuser`


## To-Do

1. Campo para adicionar autor junto com o livro

1. Feedbacks para o usuário

1. API isbn