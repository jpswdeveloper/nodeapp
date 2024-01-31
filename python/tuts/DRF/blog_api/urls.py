from django.urls import path

from .views import PostList, PostDetails

urlpatterns = [
    path("/<int:pk>/", PostDetails.as_view(), name="post detail"),
    path("", PostList.as_view(), name="create post"),
]
