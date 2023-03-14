from rest_framework import generics, views
from rest_framework.views import Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import User
from books.models import Book

from .serializers import UserSerializer

from .permissions import IsAccountOwner


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

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        user = request.user

        user.books.add(book)
        user.save()

        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        user = request.user

        user.books.remove(book)
        user.save()

        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
