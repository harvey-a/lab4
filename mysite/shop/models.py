from django.db import models
from decimal import Decimal

# Create your models here.

class time_stamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(models.Model):
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    ship_address = models.TextField()

class Product(models.Model):
    total_price = models.FloatField(max_digits=18, decimal_places=2)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length = 200)


class Cart(time_stamp):
    cart_code = models.DecimalField(decimal_places=3, max_digits=10)
    total_price = 	models.FloatField(max_digits=18, decimal_places=2, default=0.00)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField()
    quantity = models.IntegerField(default=0)
