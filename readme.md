# Projeto Django com Django Ninja

Este projeto é uma aplicação Django que utiliza Django Ninja para criar uma API rápida e eficiente.

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o projeto)

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://seu-repositorio.git
cd seu-repositorio
```
### 2. Ative o ambiente virtual
```bash
python3 -m venv env
source env/bin/activate
```
### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Criar as migrações e aplicar ao banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar um superusuário (para acessar o admin)
```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor
```bash
python manage.py runserver
```

### 7. Acessar a aplicação
    - Admin Django: http://127.0.0.1:8000/admin/
    - Documentação da API (Django Ninja Swagger): http://127.0.0.1:8000/api/docs
