from django.shortcuts import get_object_or_404
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView
)
# Create your views here. Obrigatorio usar Generic  View

class UserView(ListCreateAPIView):
    queryset = User.objects.all()