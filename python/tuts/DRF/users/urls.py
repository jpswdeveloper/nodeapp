from django.urls import path
from .views import CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView

urlpatterns = [
    path("users/", CustomUserListCreateView.as_view(), name="user-list-create"),
    path(
        "users/<int:pk>/",
        CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-detail",
    ),
]
