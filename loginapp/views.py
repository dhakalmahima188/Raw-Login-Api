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


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if the user already exists
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)

        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to create user'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

 


class UserView(APIView):
    def get(self, request):
        users = User.objects.all().values('username', 'password', 'email')
        return Response(users)


class EditProfileView(APIView):
    permission_classes = [IsAuthenticated]  
    def post(self, request):
        user = request.user  
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        print(username,email,password)
        print(user.username,user.email,user.password)

        if password:
            if user.check_password(password):
                
                if username:
                    user.username = username
                if email:
                    user.email = email
                if password:
                    user.set_password(password)

                user.save()

                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Password required'}, status=status.HTTP_400_BAD_REQUEST)
        
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
    