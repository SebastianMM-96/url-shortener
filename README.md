![django](https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png)

# URL Shortener using Django :snake:

URL Shortening Service developed in Django. 

## Virtualenv & Django :man_technologist:

Para crear un entorno virtual utilizaremos el siguiente comando:

```
$> virtualenv .
```

Una vez creado el entorno de desarrollo virtual, activalo utilizando el comando siguiente:

```
(mac) $> source bin/activate
OR
(windows) $> .\Scripts\activate
```

## Start Django project :technologist:

Realizados los pasos anteriores, ahora deberás de crear el proyecto, por lo que el comando es el siguiente:

```
$> django-admin startproject PROJECT_NAME
```

Renombra el proyecto generado por algo más común, como: 'src/'

Realiza las migraciones correspondientes utilizando los siguientes comandos:

```
$> python .\manage.py makemigrations
$> python .\manage.py migrate
```

## Superuser

Para crear un superusuario para nuestra aplicación utilizaremos las opciones que están por default

```
$> python .\manage.py createsuperuser
username: sebastianmarroquin
psw: 1234
```

## Runserver

Para ver el proyecto utilizaremos el comando:

```
$> python .\manage.py runserver
```

Y aparecerá una pantalla similar a la siguiente

![project](https://www.madelyneriksen.com/static/5f08c81718ae7596be47051995a9b61c/6da3e/django_rocket.png)

