from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from datetime import datetime, timedelta
from copies.models import Copy
from users.models import User
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    # copy = Copyserializer()
    # user = UserSerializer()

    class Meta:
        model = Loan
        fields = [
            "id",
            "loan_date",
            "expected_return",
            "is_delayed",
            "returned",
            "is_active",
            "isbn",
            "copy",
            "user",
        ]
        depth = 2

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    def update(self, instance: Loan, validated_data):
        user = User.objects.get(id=instance.user.id)
        copy = Copy.objects.get(id=instance.copy.id)
        user_loans = Loan.objects.filter(user=instance.user)
        _vals_active = {"is_active": True}
        loans__active = user_loans.filter(**_vals_active)
        _vals_delayed = {"is_delayed": True}
        loans_active_delayed = loans__active.filter(**_vals_delayed)
        if user.is_blocked:
            if not loans_active_delayed:
                date_time = datetime.now()
                expected = date_time + timedelta(days=6)
                user.blocked_until = expected

        instance.returned = datetime.today()
        copy.is_loaned = False
        instance.is_active = False
        instance.is_delayed = False
        instance.save()
        user.save()
        copy.save()

        return instance
