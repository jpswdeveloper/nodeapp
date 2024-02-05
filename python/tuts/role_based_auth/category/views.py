from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category
from .serializer import CategorySerializer


# Create your views here.
class CategoryView(APIView):
    def get(self, request, categoryId=None):
        if categoryId:
            try:
                category = Category.objects.get(pk=categoryId)
            except Category.DoesNotExist:
                return Response(
                    {"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND
                )
            categorySerializer = CategorySerializer(category)
            return Response(categorySerializer)
        else:
            category = Category.objects.all()
            categorySerializer = CategorySerializer(category, many=True)
            return Response(categorySerializer.data)

    def post(self, request):
        print({"re": request.data})
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, categoryId):
        try:
            category = Category.objects.get(pk=categoryId)
        except Category.DoesNotExist:
            return Response(
                {"error": "category is not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = CategorySerializer(
            instance=category,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, categoryId):
        try:
            category = Category.objects.get(pk=categoryId)
        except Category.DoesNotExist:
            return Response(
                {"error": "Category is not found"}, status=status.HTTP_400_BAD_REQUEST
            )
        category.delete()
        return Response({"message": "ok"})
