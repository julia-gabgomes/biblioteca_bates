from rest_framework import serializers
from .models import Copy
from django.db.models import Count


class Copyserializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = [
            "id",
            "title",
            "is_loanable",
            "book_id",
        ]

    def get_title(self, obj):
        books = obj.book.title
        return books
