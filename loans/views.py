from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from loans.models import Loan
from loans.serializers import LoanSerializer
from copies.models import Copy
from users.models import User
from books.models import Book
from .permissions import LoanPermission
from datetime import datetime, timedelta
from rest_framework.response import Response
import ipdb


# Create your views here.
# def is_weekday(data_obj):

#     if data_obj.weekday() == 5:
#      returned = returned + timedelta(days=2)

#     elif data_obj.weekday() == 6:
#      returned = returned + timedelta(days=1)
#     return returned


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
        if book.count_loaned_copies:
            return Response({"message": "No copies available"}, 401)

        copies = Copy.objects.filter(book_id=book.id)
        copy_to_loan = copies.filter(is_loaned=False)

        if copy_to_loan.count() == 0:
            return Response({"message": "No copies available"}, 401)

        date_time = datetime.now()
        returned = date_time + timedelta(days=6)
        if returned.weekday() == 5:
            returned = returned + timedelta(days=2)

        elif returned.weekday() == 6:
            returned = returned + timedelta(days=1)

        return_date = returned.strftime("%Y-%m-%d")

        one_copy = copy_to_loan.first()
        one_copy.is_loaned = True
        one_copy.save()

        serializer = self.serializer_class(
            data={
                "return_date": return_date,
                "copy": one_copy.id,
                "user": user.id,
            }
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # def perform_create(self, serializer):

        #     print(date, "ahsuhuashusaashuhauhehe")
        #     return serializer.save(return_date=date, copy= , user= )

        # serializer_class = LoanSerializer
