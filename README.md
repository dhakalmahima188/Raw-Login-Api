

# Django Login Project Documentation

### Initial Setup

#### Setup Virtual Environment

```shell
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
```


#### Install Django
```shell
pip install django
django-admin startproject loginproject
python manage.py runserver
python manage.py startapp loginapp
python manage.py createsuperuser
```

#### Apply database migrations
```shell
python manage.py makemigrations
python manage.py migrate
```


### Establish database connection:
```shell
conn = psycopg2.connect(
           host="localhost",
           port="5432",
           database="postgres",
           user="postgres",
           password="mahima@123"
       )
```


### Create Table
#### urls.py
```shell
path('createTable/', CreateTableView.as_view(), name='createTable'),
```

#### views.py
```shell
cur.execute('''CREATE TABLE IF NOT EXISTS employees
                       (id SERIAL PRIMARY KEY,
                       username TEXT NOT NULL,
                       email TEXT NOT NULL,
                       password TEXT NOT NULL)''')
```

### Update Table
#### urls.py
```shell
path('UpdateTable/', UpdateTableView.as_view(), name='UpdateTable'),
```

#### views.py
```shell
dict1 = {
           "username": "username",
           "password": "password",
           "email": "email"
       }
       cur.execute(
           "INSERT INTO employees (username, password, email) VALUES (%(username)s, %(password)s, %(email)s);", dict1)
```
