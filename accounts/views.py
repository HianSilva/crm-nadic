from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class LoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('products-list')

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')