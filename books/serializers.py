from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book
import ipdb
from copies.models import Copy


class BookSerializer(serializers.ModelSerializer):
    count_copies = serializers.SerializerMethodField()
    count_loaned_copies = serializers.SerializerMethodField()

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
            "count_loaned_copies",
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
        return obj.copies.all().count()

    def get_count_loaned_copies(self, obj: Book):
        copy = Copy.objects.filter(book_id=obj.id)
        return copy.filter(is_loaned=False).count()
