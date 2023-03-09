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
        isbn = self.request.data["isbn"]
        user = get_object_or_404(User, id=self.kwargs.get("user_id"))
        if user.is_blocked:
            return Response({"message": "User has books to return"}, 401)

        # loan = Loan.objects.filter(isbn=isbn)
        # if loan:
        #     return Response(
        #         {"message": "This user already have a copy with this isbn"}, 401
        #     )

        book = get_object_or_404(Book, isbn=isbn)
        if book.count_loaned_copies:
            return Response({"message": "No copies available"}, 401)

        copies = Copy.objects.filter(book_id=book.id)
        copy_to_loan = copies.filter(is_loaned=False)

        if copy_to_loan.count() == 0:
            return Response({"message": "No copies available"}, 401)

        date_time = datetime.now()
        expected = date_time + timedelta(days=6)
        if expected.weekday() == 5:
            expected = expected + timedelta(days=2)

        elif expected.weekday() == 6:
            expected = expected + timedelta(days=1)

        expected_date = expected.strftime("%Y-%m-%d")

        one_copy = copy_to_loan.first()
        one_copy.is_loaned = True
        one_copy.save()

        serializer = self.serializer_class(
            data={
                "expected_return": expected_date,
                "copy": one_copy.id,
                "user": user.id,
                "isbn": isbn,
            }
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoanReturnView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [LoanPermission]
    queryset = Loan.objects.all()
    lookup_url_kwarg = "user_id"
    serializer_class = LoanSerializer

    # def perform_update(self, serializer):
    # isbn = self.request.data["isbn"]
    # id_copy = serializer.data["copy"]
    # user = get_object_or_404(User, id=self.kwargs.get("user_id"))
    # loan = get_object_or_404(Loan, isbn=isbn)
    # copy = get_object_or_404(Copy, id=id_copy)

    # loan.returned = datetime.today()
    # loan.is_active = False
    # copy.is_loaned = False
    # loan.is_delayed = False

    # copy.save()
    # loan.save()
    # serializer = LoanSerializer(loan)

    # return Response(status=201)
