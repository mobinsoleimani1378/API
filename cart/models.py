from account.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.CharField(max_length=30)
    created_ad = models.DateTimeField(auto_now_add=True)
    adress = models.TextField()

    def __str__(self):
        return self.user.fullname


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item')
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=30, null=True, blank=True)
    quantity = models.CharField(max_length=30)
    price = models.PositiveIntegerField(null=True, blank=True)


