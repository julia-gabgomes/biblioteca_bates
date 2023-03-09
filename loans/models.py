from django.db import models


class Loan(models.Model):
    loan_date = models.DateTimeField(auto_now_add=True)
    expected_return = models.DateField()
    is_delayed = models.BooleanField(default=False, blank=False)
    returned = models.DateTimeField(blank=True)
    is_active = models.BooleanField(default=True, blank=False)

    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.RESTRICT, related_name="loans"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="loans"
    )
