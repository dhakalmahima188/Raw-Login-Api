from . import views
from django.urls import path
from .views import LoginView,RegisterView,EditProfileView,UserView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import send_email



urlpatterns = [
     path('', views.Home, name='Home'),
     path('api/login/', LoginView.as_view(), name='login'),
     path('send-email/', send_email, name='send_email'),
     path('api/register/', RegisterView.as_view(), name='register'),
     path('api/editprofile/', EditProfileView.as_view(), name='register'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/users/', UserView.as_view(), name='users'),
     ]