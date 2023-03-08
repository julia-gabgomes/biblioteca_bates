from django.urls import path
from . import views

urlpatterns = [
    path("books/<int:book_id>/loan", views.BookView.as_view()),
    path("books/<int:book_id>/return", views.BookRetrieveAPIView.as_view()),
]
