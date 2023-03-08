from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from loans.models import Loan
from loans.serializers import LoanSerializer
from copies.models import Copy
from users.models import User
from books.models import Book
from .permissions import LoanPermission
from datetime import datetime
from rest_framework.response import Response
import ipdb

# Create your views here.


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [LoanPermission]
    queryset = Loan.objects.all()
    lookup_url_kwarg = "user_id"
    serializer_class = LoanSerializer

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get("user_id"))
        if user.is_blocked:
            return Response({"message": "User has books to return"}, 401)

        book = get_object_or_404(Book, isbn=self.request.data["isbn"])
        if book.count_loaned_copies == 0:
            return Response({"message": "No copies available"}, 401)

        copies = Copy.objects.filter(book_id=book.id)
        copy_to_loan = copies.filter(is_loaned=False)
        copy_to_loan[0].is_loaned = True
        # copy_to_loan.save()
        date = datetime.today()
        # serializer = LoanSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        LoanSerializer(return_date=date, copy=copy_to_loan[0], user=user)
        return super().post(request, *args, **kwargs)

    # def perform_create(self, serializer):

    #     print(date, "ahsuhuashusaashuhauhehe")
    #     return serializer.save(return_date=date, copy= , user= )

    serializer_class = LoanSerializer
