from django.urls import path
from .views import CategoryView

urlpatterns = [
    path("category/<int:categoryId>", CategoryView.as_view()),
    path("category/", CategoryView.as_view()),
]
