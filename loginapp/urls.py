from django.urls import path

from loginapp.views import (
    SendEmailView,
    HomeView,
    CreateTableView,
    UpdateTableView,
    GetEmployeesView,
    GetEmployeeView,
    DeleteEmployeeView,
    AddEmployeeView,
    LoginView,
    RegisterView,
    TokenView,
    EditView,
    DeactivateView,
    MakeAdminView
    
)

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('send-email/', SendEmailView.as_view(), name='send_email'),
    path('createTable/', CreateTableView.as_view(), name='createTable'),
    path('UpdateTable/', UpdateTableView.as_view(), name='UpdateTable'),
    path('get_employees/', GetEmployeesView.as_view(), name='get_employees'),
    path('get_employee/<int:id>/', GetEmployeeView.as_view(), name='get_employee'),
    path('delete_employee/<int:id>/', DeleteEmployeeView.as_view(), name='delete_employee'),
    path('add_employee/', AddEmployeeView.as_view(), name='add_employee'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/<int:id>', RegisterView.as_view(), name='register'),
    path('get_token/<int:id>',TokenView.as_view(), name='get_token'),
    path('edit/<int:id>', EditView.as_view(), name='edit'),
    path('deactivate/<int:id>', DeactivateView.as_view(), name='deactivate'),
    path('make_admin/<int:id>', MakeAdminView.as_view(), name='make_admin'),
    
]
