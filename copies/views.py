from asyncio import mixins
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from books.permissions import BookPermission
from .serializers import Copyserializer
from .models import Copy
from books.models import Book


# Create your views here.
class CopyView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [BookPermission]

    queryset = Copy.objects.all()
    serializer_class = Copyserializer
    lookup_url_kwarg = "book_id"

    def perform_create(self, serializer):
        book_obj = self.kwargs.get("book_id")
        serializer.save(book=get_object_or_404(Book, id=book_obj))

    def get_queryset(self):
        book_id = self.kwargs.get(self.lookup_url_kwarg)
        copies = Copy.objects.filter(book_id=book_id)
        return copies


class CopyRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = Copyserializer
    lookup_url_kwarg = "book_id"
