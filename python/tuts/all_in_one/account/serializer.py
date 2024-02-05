from rest_framework import serializers
from ..user.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class AuthSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise ValidationError(e.message)
        return value

    def validate(self, data):

        email = data.get("email")
        if not email:
            raise ValidationError("Email is required.")

        # You can add more validation for other fields as needed
        return data

    class Meta:
        model = User
        field = ["email", "password"]
