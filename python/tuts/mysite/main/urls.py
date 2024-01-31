from django.urls import path

# Import all get routes into urls page
from . import views

urlpatterns = [
    # Route directory comes from parent route going to be created in main
    path("", views.index, name="index"),
    path("<int:id>", views.v1, name="v1"),
]
