from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer

class SignupView(generics.CreateAPIView):
    """
    Endpoint para criar uma nova conta de usuário.
    Por padrão, o novo usuário é adicionado ao grupo 'Vendedor'.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
