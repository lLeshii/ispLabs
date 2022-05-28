from django.db import models
from django.contrib.auth.models import User
from drug_store.models import Product
# Create your models here.


class Order(models.Model):
    ORDER_STATUS = (
        ("processing", "processing"),
        ("delivering", "delivering"),
        ("received", "received")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    status = models.CharField(choices=ORDER_STATUS, default="PENDING", max_length=10)

    def get_cost(self):
        return self.amount * self.product.price
