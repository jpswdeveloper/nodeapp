from rest_framework import serializers

# from product.serializer import ProductSerializer
from .models import Seller
from account.serializer import UserSerializer


class UserRelatedSerializer(serializers.StringRelatedField):
    def to_representation(self, value):
        return UserSerializer(value).data


# def to_internal_value(self, data):


class SellerSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True)
    user = UserRelatedSerializer()

    class Meta:
        model = Seller
        fields = "__all__"
