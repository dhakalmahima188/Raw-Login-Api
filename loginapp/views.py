from django.http import HttpResponse
from django.core.mail import send_mail
import psycopg2


def send_email(request):
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="mahima@123")

    recipient_list = []
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_emails")
    rows = cur.fetchall()
    for row in rows:

        column2 = row[1]
        recipient_list.append(column2)
        print(column2)
    cur.close()
    conn.close()

    subject = 'Invitation-link'
    message = 'Register for the event by clicking the link below:we neded to send a token here'
    from_email = 'mahi.testmail18@gmail.com'  # Replace with your email address

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse('Email sent successfully')


def Home(request):
    return HttpResponse("Hello People, Have a good day !!!")

def createTable(request):
    conn=psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="mahima@123",
    )
    cur=conn.cursor()
    cur.execute("CREATE TABLE employees (id serial PRIMARY KEY, username VARCHAR,password VARCHAR, email VARCHAR);")
    conn.commit()
    conn.close()
    return HttpResponse("Table created successfully")

def UpdateTable(request):
    conn=psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="mahima@123",
    )
    cur=conn.cursor()
    dict1={
        "username":"xyz",
        "password":"xyz",
        "email":"dhakalmahima18@gmail.com"
    }
    cur.execute("INSERT INTO employees (username,password,email) VALUES (%(username)s,%(password)s,%(email)s);",dict1)
    conn.commit()
    conn.close()
    return HttpResponse("Table updated successfully")


class EmployeesView:
    def get(self, request):
        return HttpResponse('Hello, Welcome to GeeksforGeeks')