from django.db import models


class Loan(models.Model):
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    is_delayed = models.BooleanField(default=False, blank=False)

    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.RESTRICT, related_name="loans"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="loans"
    )
