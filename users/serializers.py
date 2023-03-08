from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

import ipdb


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token


class UserSerializer(serializers.ModelSerializer):

    # books = serializers.SerializerMethodField()

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
            "books",
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

    # def get_books(self, user):
    #     # ipdb.set_trace()
    #     books = user.books.all()
    #     return books
