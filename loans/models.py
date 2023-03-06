from django.db import models


class Loan(models.Model):
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    is_delayed = models.BooleanField(default=False , blank=False)

    copy_id = models.ForeignKey(
        "copies.Copy", on_delete=models.RESTRICT, related_name="loans"
    )
    user_id = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="loans"
    )
