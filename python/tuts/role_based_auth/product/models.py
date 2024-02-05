from django.db import models
from django.utils import timezone
from category.models import Category
from seller.models import Seller


# Create your models here.
class Product(models.Model):
    price = models.FloatField(
        null=False,
    )
    name = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ManyToManyField(Seller)
