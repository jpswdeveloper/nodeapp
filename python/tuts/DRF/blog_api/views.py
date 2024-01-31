from rest_framework import generics
from blog.models import Category, Post
from .serializers import PostSerializer

# List Create API View Responsible for write and read
# Retrieve Update Destroy API View Responsible for read, update and delete


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
