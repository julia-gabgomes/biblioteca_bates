from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "isbn",
            "title",
            "author",
            "publisher",
            "edition",
            "genre",
            "language",
            "pages_number",
        ]
        extra_kwargs = {
            "isbn": {
                "validators": [
                    UniqueValidator(
                        queryset=Book.objects.all(),
                        message="isbn already exists, must be unique,",
                    )
                ]
            },
        }
