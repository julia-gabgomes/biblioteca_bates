from django.shortcuts import get_list_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer
from .permissions import BookPermission


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [BookPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [BookPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "book_id"
