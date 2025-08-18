from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class LoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = '/products/'

class LogoutView(LogoutView):
    next_page = 'login'