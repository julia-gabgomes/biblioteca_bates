from rest_framework import serializers
from .models import Copy
from django.db.models import Count


class Copyserializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    count_copies = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = [
            "id",
            "title",
            "is_prime",
            "is_loaned",
            "book_id",
            "count_copies",
        ]

    def get_title(self, obj):
        books = obj.book.title
        return books

    def get_count_copies(self, obj):
        return Copy.objects.filter(book=obj.book).count()
