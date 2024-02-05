from rest_framework import serializers
from .models import Category
from django.core.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def validate(self, data):
        if data["name"] is None:
            raise ValidationError("Category name is must be set")
        return data

    def create(self, data):
        categories = Category.objects.create(**data)
        return categories

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
