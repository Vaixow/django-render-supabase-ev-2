# TAREA-UNIDAD-2-BACKEND

C:\ProgramData\anaconda3\Scripts\activate.bat

python -m venv venv

venv\Scripts\activate

requirements:
django
python-dotenv
gunicorn
whitenoise
psycopg[binary,pool]
psycopg2

pip install -r requirements.txt

Configuramos postgresql en settings.py:

Pegamos esto:

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


Y modificamos esto:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

A esto:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("dbname"),
        "USER": os.getenv("user"),
        "PASSWORD": os.getenv("password"),
        "HOST": os.getenv("host"),
        "PORT": os.getenv("port"),
    }
}

Creamos variables de entorno con archivo .env
Credenciales de connect -> Transaction pooler 

user=USER
password=PASSWORD
host=HOST
port=PORT
dbname=NAME

creamos superuser:

python manage.py createsuperuser

aplicamos migraciones:
python manage.py makemigrations
python manage.py migrate
