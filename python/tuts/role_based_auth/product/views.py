from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer


# Create your views here.
class ProductView(APIView):
    def get(self, request, productId=None):
        print({"request": request})
        if productId:
            try:
                product = Product.objects.get(pk=productId)
            except Product.DoesNotExist:
                return Response(
                    {"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND
                )
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, productId):
        try:
            Product = Product.objects.get(pk=productId)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product is not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductSerializer(
            instance=Product,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productId):
        try:
            Product = Product.objects.get(pk=productId)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product is not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        Product.delete()
        return Response({"message": "ok"})
