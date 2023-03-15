from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token


class UserSerializer(serializers.ModelSerializer):

    followed_books = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "is_blocked",
            "is_employee",
            "followed_books",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(User.objects.all(), "This field must be unique.")
                ],
                "required": True,
            },
        }

    def create(self, validated_data: dict):
        super_user = validated_data.get("is_employee")
        if super_user:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        has_password = validated_data.get("password", None)
        if has_password:
            instance.set_password(has_password)
            validated_data.pop("password")
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    @extend_schema_field(OpenApiTypes.ANY)
    def get_followed_books(self, user):
        books = user.books.all()
        books_info = []

        for book in books:
            books_info.append({"title": book.title, "author": book.author})

        return books_info
