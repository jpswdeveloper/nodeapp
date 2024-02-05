from django.urls import path
from .views import SellerView

urlpatterns = [
    path("seller/<int:sellerId>", SellerView.as_view()),
    path("seller/", SellerView.as_view()),
]
