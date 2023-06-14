from django.core.mail import send_mail
from django.http import HttpResponse,HttpRequest
from rest_framework.views import APIView
from rest_framework import status, response
import psycopg2
from .serializers import EmployeeSerializer
from django.shortcuts import  redirect
from .serializers import EmployeeSerializer
from datetime import datetime, timedelta
from urllib.parse import urlencode
import jwt

class SendEmailView(APIView):
    def get_connection():
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="mahima@123"
        )
        return conn

    def get(self, request):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:             
            id=row[0] 
            username=row[1] 
            password=row[3]
            send_to_mail=row[2]    
            print(id,username,password,send_to_mail)
            token=TokenView.get_token(self,request,id)
            print(token)
            subject = 'Invitation-link'
            message = f'Register for the event by clicking the link below:  {token}'
            from_email = 'mahi.testmail18@gmail.com'  # settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [send_to_mail])
        cur.close()
        conn.close()
        return HttpResponse('Email sent successfully')

class EditView(APIView):
    def get(self,request,id):
        
        user_id=int(request.COOKIES.get('id'))
        
        if user_id==id:
            conn = SendEmailView.get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
            row = cur.fetchone()

            if row:
                employee = {
                    'id': row[0],
                    'username': row[1],
                    'email': row[2],
                    'password': row[3],
                }
                response_data = {
                    'employee': employee,
                }
                return response.Response(response_data)
            else:
                return response.Response({'error': 'Employee not found'}, status=404)
        else:
            return response.Response("You are not authorized to edit this profile")
        
    def post(self,request,id):
        
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        print(id,username,email,password)
        
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        
        cur.execute("UPDATE employees SET username = %s, email= %s, password= %s WHERE id= %s", [username,email,password,id]  )
        cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
        result=cur.fetchone()
        print(result)
        conn.commit()
        return response.Response("Profile edited successfully")
        
class TokenView(APIView):
       def get_token(self, request, id):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
        row = cur.fetchone()

        if row:
            employee = {
                'id': row[0],
                'username': row[1],
                'email': row[2],
                'password': row[3],
            }

            id = employee['id']
            token_lifetime = timedelta(days=1)
            token_expiry = datetime.now() + token_lifetime
            access_token = jwt.encode(
                {
                    'id': employee['id'],
                    'username': employee['username'],
                    'email': employee['email'],
                    'password': employee['password'],
                    'exp': int(token_expiry.timestamp())
                },
                'secret9742357373',
                algorithm='HS256'
            )

            token = access_token

            base_url = f"http://127.0.0.1:8000/register/{id}"
            query_params = {'token': token}

            registration_link = base_url + '?' + urlencode(query_params)
            return registration_link

        return response.Response("Employee not found.")


class HomeView(APIView):
    def get(self, request):
        return response.Response("Hello People, Have a good day !!!")


class CreateTableView(APIView):
    def get(self, request):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS employees
                        (id SERIAL PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL,
                        is_active BOOLEAN DEFAULT FALSE)''')
        conn.commit()
        conn.close()
        return response.Response("Table created successfully")


class UpdateTableView(APIView):
    def get(self, request):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        dict1 = {
            "username": "xyz",
            "password": "xyz",
            "email": "dhakalmahima18@gmail.com",
            "is_active": False
        }
        cur.execute(
            "INSERT INTO employees (username, password, email,is_active) VALUES (%(username)s, %(password)s, %(email)s,%(is_active)s);", dict1)
        conn.commit()
        conn.close()
        return response.Response("Table updated successfully")


class GetEmployeesView(APIView):
    def get(self, request):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        employees = []

        for row in rows:
            employee = {
                'id': row[0],
                'username': row[1],
                'email': row[2],
                'password': row[3],
                'is_active': row[4] if row[4] else False
            }
            employees.append(employee)

        response_data = {
            'employees': employees,
        }

        return response.Response(response_data)


class RegisterView(APIView):
    def get(self, request,id):
        print(id)
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        employees = []

        for row in rows:
            employee = {
                'id': row[0],
                'username': row[1],
                'email': row[2],
                'password': row[3],
                 'is_active': row[4] if row[4] else False
            }
            employees.append(employee)

        response_data = {
            'employees': employees,
        }

        return response.Response(response_data)
    
    
    def post(self,request,id):
        if request.method == 'POST':
            token = request.GET.get('token')
            password = request.data.get('password')
            username=request.data.get('username')             
            decoded_token = jwt.decode(token, 'secret9742357373', algorithms=['HS256'])           
            email = decoded_token.get('email')
       
            conn = SendEmailView.get_connection()
          
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT email FROM employees WHERE id = %s", [id])
                result = cursor.fetchone()
               
                if result:
                   
                    print(result[0],email,id)
                    is_active=True
                    # Update the employee password with the entered password
                    cursor.execute("UPDATE employees SET password = %s, username= %s, is_active=%s WHERE id= %s and email = %s", [
                                   password,username,is_active,id, email]  )
                    conn.commit()
                    
                    # Redirect to login page after successful registration
                    return response.Response("Password updated successfully")

            # Handle the case when the employee doesn't exist or the token is invalid
            return redirect('invalid-token')

        # Get the email from the token and pass it to the template
        token = request.GET.get('token')
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT email FROM employee WHERE token = %s", [token])
            result = cursor.fetchone()
            if result:
                email = result[0]
            else:
                email = ""

            return response.Response({'email': email})


class LoginView(APIView):   
        
    def post(self, request):
        print(request.data, type(request.data))
        # email=request.data['email']
        # or
        serializer = EmployeeSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            username= serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            password=serializer.validated_data.get('password')
            print(username,email,password)
 
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM employees ")
        rows = cur.fetchall()
        login_successful = False

        for row in rows:
            print(row[0],row[1], row[2], row[3],row[4])
            if row[1] == username and row[2] == email and row[3] == password and row[4]==True:
                login_successful = True
                break
        response1=HttpResponse()
        if login_successful:
            response1 = response.Response("Login successful")
            response1.set_cookie('id', row[0])        
             
            return response1
        else:
            return response.Response("Invalid credentials")
            



class GetEmployeeView(APIView):
    def get(self, request, id):
        print(id)
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
        row = cur.fetchone()

        if row:
            employee = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
            }
            response_data = {
                'employee': employee,
            }
            return response.Response(response_data)
        else:
            return response.Response({'error': 'Employee not found'}, status=404)


class DeleteEmployeeView(APIView):
    def get(self, request, id):
        print(id)
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM employees WHERE id = %s", (id,))
        conn.commit()
        return response.Response("Employee deleted successfully")


class AddEmployeeView(APIView):
    def post(self, request):
        print(request.data, type(request.data))
        # email=request.data['email']
        # or
        serializer = EmployeeSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            print(email)

        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO employees (username, password, email) VALUES (%s, %s, %s)", ('xyz', 'abc', email))
        conn.commit()

        return response.Response("Employee added successfully.")
    
class DeactivateView(APIView):
    def post(self,request,id):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE employees SET is_active = %s WHERE id= %s", [False,id]  )
        return response.Response("Employee deactivated successfully")
        