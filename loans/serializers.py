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
            "isbn",
            "copy",
            "user",
        ]
        # extra_kwargs = {
        #     "isbn": {
        #         "validators": [
        #             UniqueValidator(Loan.objects.all(), "This field must be unique.")
        #         ],
        #         "required": True,
        #     },
        # }

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)

    # def get_title_book(self, obj):
    #     return obj.copy.title_book
