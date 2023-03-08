from django.shortcuts import get_object_or_404, get_list_or_404
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import views

from books.models import Book
from books.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
import ipdb

# Create your views here. Obrigatorio usar Generic views


class UserView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        user = request.user

        user.books.add(book)
        user.save()

        serializer = UserSerializer(user)

        return Response(serializer.data, status=200)
