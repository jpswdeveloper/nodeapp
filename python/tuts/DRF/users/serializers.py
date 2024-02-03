# responsiblity to validate
# responsiblity to to check validated data || email if its unique or not
# let native python data to json data
# responsiblity to validate

from rest_framework import serializers
from .models import CustomizedUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class CustomizedUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model: CustomizedUser
        field: ["id", "email", "phone", "address", "is_staff", "is_active"]

    # Functions checks out password
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    # Functions checks out email

    def validate_email(self, value):
        if CustomizedUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    # Create functionality
    def create(self, validated_data):
        instance = CustomizedUser.objects.create_user(**validated_data)
        return instance
