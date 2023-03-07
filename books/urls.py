from django.urls import path
from . import views
from copies.views import CopyView, CopyRetrieveAPIView

urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:book_id>/", views.BookRetrieveAPIView.as_view()),
    path("books/<int:book_id>/copy/", CopyView.as_view()),
    path("books/<int:book_id>/copyretriever/", CopyRetrieveAPIView.as_view()),
]
