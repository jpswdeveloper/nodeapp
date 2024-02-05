from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Seller
from .serializer import SellerSerializer


# Create your views here.
class SellerView(APIView):
    def get(self, request, sellerId=None):

        if sellerId:
            try:
                seller = Seller.objects.get(pk=sellerId)
            except Seller.DoesNotExist:
                return Response(
                    {"message": "Seller not found"}, status=status.HTTP_404_NOT_FOUND
                )
            sellerSerializer = SellerSerializer(seller)
            return Response(sellerSerializer.data)
        else:
            seller = Seller.objects.all()
            sellerSerializer = SellerSerializer(seller, many=True)
            return Response(sellerSerializer.data)

    def post(self, request):
        serializer = SellerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, SellerId):
        try:
            seller = Seller.objects.get(pk=SellerId)
        except Seller.DoesNotExist:
            return Response(
                {"error": "Seller is not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = SellerSerializer(
            instance=seller,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, SellerId):
        try:
            seller = Seller.objects.get(pk=SellerId)
        except Seller.DoesNotExist:
            return Response(
                {"error": "Seller is not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        seller.delete()
        return Response({"message": "ok"})
