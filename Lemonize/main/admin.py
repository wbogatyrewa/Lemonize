from django.contrib import admin
from .models import Product, Basket, Order


admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)