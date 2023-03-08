from django.db import models


class Copy(models.Model):
    is_prime = models.BooleanField(default=False)
    is_loaned = models.BooleanField(default=False)

    book = models.ForeignKey(
        "books.Book", on_delete=models.PROTECT, related_name="copies"
    )
