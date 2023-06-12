

# Django Login Project Documentation

## Initial Setup

### Setup Virtual Environment

```shell
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
```


### Install Django
```shell
pip install django
django-admin startproject loginproject
python manage.py runserver
python manage.py startapp loginapp
python manage.py createsuperuser
```

### Apply database migrations
```shell
python manage.py makemigrations
python manage.py migrate
```

