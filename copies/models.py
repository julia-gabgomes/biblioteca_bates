from django.db import models


class Copy(models.Model):
    is_loanable = models.BooleanField(default=False)

    book_id = models.ForeignKey(
        "books.Book", on_delete=models.PROTECT, related_name="copies"
    )
