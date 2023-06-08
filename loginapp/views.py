from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
import psycopg2
import json
from .serializers import EmployeeSerializer
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
    
    def post(self, request):
        conn = SendEmailView.get_connection()

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
        message = 'Register for the event by clicking the link below: we neded to send a token here'
        from_email = 'mahi.testmail18@gmail.com'  # Replace with your email address

        send_mail(subject, message, from_email, recipient_list)
        return HttpResponse('Email sent successfully')

class HomeView(APIView):
    def get(self, request):
        return HttpResponse("Hello People, Have a good day !!!")

class CreateTableView(APIView):
    def get(self, request):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS employees
                        (id SERIAL PRIMARY KEY,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL)''')
        conn.commit()
        conn.close()
        return HttpResponse("Table created successfully")

class UpdateTableView(APIView):
    def get(self, request):
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        dict1 = {
            "username": "xyz",
            "password": "xyz",
            "email": "dhakalmahima18@gmail.com"
        }
        cur.execute("INSERT INTO employees (username, password, email) VALUES (%(username)s, %(password)s, %(email)s);", dict1)
        conn.commit()
        conn.close()
        return HttpResponse("Table updated successfully")

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
                'name': row[1],
                'email': row[2],
            }
            employees.append(employee)

        response_data = {
            'employees': employees,
        }

        return JsonResponse(response_data)

class RegisterView(APIView):
    def get(self, request):
        return HttpResponse("Hello People, Have a good day !!!")

class LoginView(APIView):
    def get(self, request):
        return HttpResponse("Hello People, Have a good day !!!")

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
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Employee not found'}, status=404)

class DeleteEmployeeView(APIView):
    def get(self, request, id):
        print(id)
        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM employees WHERE id = %s", (id,))
        conn.commit()
        return HttpResponse("Employee deleted successfully")
    

class AddEmployeeView(APIView):
    def post(self, request):
        print(request.data,type(request.data))
        #email=request.data['email']
        #or
        serializer = EmployeeSerializer(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            print(email)

        conn = SendEmailView.get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO employees (username, password, email) VALUES (%s, %s, %s)", ('xyz', 'abc', email))
        conn.commit()

        return HttpResponse("Employee added successfully.")

