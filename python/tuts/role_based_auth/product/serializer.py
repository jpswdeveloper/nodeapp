from rest_framework import serializers
from .models import Product
from django.core.exceptions import ValidationError
from seller.serializer import SellerSerializer

from seller.models import Seller


class ProductRelatedSellerSerializer(serializers.StringRelatedField):
    def to_representation(self, value):
        return SellerSerializer(value).data

    def to_internal_value(self, data):
        return data

        # def create(self, validated_data):
        # seller_ids = validated_data.pop("seller", None)
        # print(seller_ids)
        # instance = self.Meta.model(**validated_data)
        # instance.save()
        # instance.seller.add(*seller_ids)  # Add sellers after saving the instance
        # instance.save()
        # return instance


class ProductSerializer(serializers.ModelSerializer):
    seller = ProductRelatedSellerSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    def validate(self, data):
        if data["name"] is None:
            raise ValidationError("Product name is must be set")
        return data

    def create(self, data):
        seller_ids = data.pop("seller", [])
        instance = self.Meta.model(**data)
        instance.save()
        instance.seller.add(*seller_ids)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
