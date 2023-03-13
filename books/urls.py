from django.urls import path
from . import views
from copies.views import CopyView, CopyRetrieveAPIView
from loans.views import LoanView, LoanReturnView
from users.views import FollowAPIView


urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:book_id>/", views.BookRetrieveAPIView.as_view()),
    path("books/<int:book_id>/copy/", CopyView.as_view()),
    path("books/<int:book_id>/copyretriever/", CopyRetrieveAPIView.as_view()),
    path("books/<int:book_id>/follow/", FollowAPIView.as_view()),
    path("books/<int:user_id>/loan/", LoanView.as_view()),
    path("books/<int:loan_id>/return/", LoanReturnView.as_view()),
]
