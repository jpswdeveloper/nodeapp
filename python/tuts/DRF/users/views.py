from django.shortcuts import render
from .models import CustomizedUser
from .serializers import CustomizedUserSerializer
from rest_framework import generics
from rest_framework.response import Response

# Import your serializer
# import your model
# Create your views here.
# import generics


class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomizedUser.objects.all()
    serializer = CustomizedUserSerializer(queryset, many=True)


class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomizedUser.objects.all()
    serializer_class = CustomizedUserSerializer(queryset, many=True)
