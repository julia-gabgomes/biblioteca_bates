from django.db import models


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=17, unique=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=100)
    edition = models.DateField()
    genre = models.CharField(max_length=50, null=True)
    language = models.CharField(max_length=50)
    pages_number = models.IntegerField()
    count_loaned_copies = models.IntegerField(default=0)
