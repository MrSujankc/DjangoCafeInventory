
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import UserRegisterView


app_name = "members"


urlpatterns = [
   path('members/login/', LoginView.as_view(template_name='members/login.html'), name='login'),
   path("register/", UserRegisterView.as_view(), name='register'),
  
]