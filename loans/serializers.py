from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from copies.models import Copy
from .models import Loan
from users.serializers import UserSerializer


class LoanSerializer(serializers.ModelSerializer):
    title_book = serializers.CharField(source="copy.book.title")
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
            "title_book",
        ]
        depth = 2

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        copy = get_object_or_404(Copy, id=instance.copy_id)


        instance.returned = datetime.today()
        copy.is_loaned = False
        instance.is_active = False
        instance.is_delayed = False
        instance.save()
        copy.save()

        return instance
