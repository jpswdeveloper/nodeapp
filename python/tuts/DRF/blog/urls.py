from django.urls import path

from .views import blogone

# app_name = "blog"

urlpatterns = [path("", blogone)]
