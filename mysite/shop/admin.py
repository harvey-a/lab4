from django.contrib import admin
from shop.models import User, Product, Cart

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)