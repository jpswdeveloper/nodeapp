from django.db import models
from account.models import User


# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_earn_amount = models.FloatField(null=False, default=0)
    total_spent_amount = models.FloatField(null=False, default=0)
    shop_name = models.CharField(max_length=15, null=False)

    def __str__(self) -> str:
        return f"{self.shop_name} - {self.user.email}"
