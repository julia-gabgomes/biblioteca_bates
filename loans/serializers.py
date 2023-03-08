from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["id", "loan_date", "is_delayed", "return_date", "copy", "user"]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)
