# Login-Project-APIS
#### * Scripts to connect postgres and manual data entry without models.
#### * No use of MODELS.PY: only changes in views.py and urls.py
#### * Login and Register APis
#### * Apis for user display
#### * simple jwt tokenization for acess and refresh
#### * authorization and edit user profile via postman only!


# Django Login Project Documentation

## Initial Setup

To set up the project, follow these steps:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Django
pip install django

# Create Django project
django-admin startproject loginproject

# Start Django development server
python manage.py runserver

# Create Django app
python manage.py startapp loginapp

# Create superuser
python manage.py createsuperuser

# Apply database migrations
python manage.py makemigrations
python manage.py migrate
```