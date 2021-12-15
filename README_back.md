# Developping back
-------------------
Linux, dist Ubuntu 20.04.

## Install virtual environment
-------------------------------------------------
$ sudo apt install python3-virtualenv

## create virtual environment
-----------------------------------------------
$ virtualenv entorno_virtual -p python3

## activate virtual environment
-----------------------------------------------
$ source entorno_virtual/bin/activate

## Desativate virtual environment
------------------------------------
$ deativate

## Install dependencies
------------------------------
$ pip install -r requirements.txt

## create database y postgres
I've got an user in my postgres in local, called javier with password: 2525_ap
Change postgres'configuration as your convinience.
$ psql -d postgres -U javier
-create DB
CREATE DATABASE apiumm WITH OWNER javier;
-change settings in django:
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'apiumm',
        'USER': 'javier',
        'PASSWORD': '2525_ap',
        'HOST': 'localhost',
        'PORT': '5432'
    },

# make migrations, from the folder where manage.py is located
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# create a superuser
------------------------------
$ python3 manage.py createsuperuser
user: javier
pss: 89_Lp%wD

# run the server
------------------------------
$ back/python3 manage.py runserver

# create an app
------------------------------
$ python manage.py startapp booking
move the app to apps folder and change configuration

# create model
------------------------------
models.py
makemigrations & migrate

# create an app
------------------------------
$ python manage.py startapp api
move the app to apps folder and change configuration
create file api/urls.py

# endpoints back
------------------------------
http://localhost:8000/
http://localhost:8000/admin/
http://127.0.0.1:8000/api/v1/token/
http://127.0.0.1:8000/api/v1/token/refresh/
http://localhost:8000/api/v1/

## run tests
-------------------------------
$ back/python3 manage.py test ./main/apps/booking/test