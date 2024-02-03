from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomizedUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email
