from . import views
from django.urls import path
from .views import send_email



urlpatterns = [
     path('', views.Home, name='Home'),  
     path('send-email/', send_email, name='send_email'),
     
     ]