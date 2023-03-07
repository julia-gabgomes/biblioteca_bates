from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book
import ipdb
from copies.models import Copy


class BookSerializer(serializers.ModelSerializer):
    count_copies = serializers.SerializerMethodField()

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
            "count_copies",
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

    def get_count_copies(self, obj: Book):
        # books = Copy.objects.filter(book_id=obj.book_id).count()
        return obj.copies.all().count()
