# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email field must be set")

        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=100, null=False)
    profile_pic = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
