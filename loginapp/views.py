from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
import psycopg2

def send_email(request):
    subject = 'Invitation-link'
    message = 'Register for the event by clicking the link below: http://127.0.0.1:8000/api/register/'
    from_email = 'mahi.testmail18@gmail.com' # Replace with your email address
    recipient_list = ['076bct033.mahima@pcampus.edu.np', 'dhakalmahima18@gmail.com']  # Replace with recipient email addresses

    send_mail(subject, message, from_email, recipient_list)

    # Optionally, you can redirect or return a response
    return HttpResponse('Email sent successfully')

def Home(request):
    return HttpResponse("Hello People, Have a good day !!!")

def fetchemails(request):
    conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="mahima@123")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_emails")
    rows = cur.fetchall()
    