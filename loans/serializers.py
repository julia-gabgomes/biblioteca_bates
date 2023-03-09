from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    # title_book = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = [
            "id",
            "loan_date",
            "expected_return",
            "is_delayed",
            "returned",
            "is_active",
            "copy",
            "user",
        ]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    # def get_title_book(self, obj):
    #     return obj.copy.title_book
