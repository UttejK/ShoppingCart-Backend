from django.contrib import admin

# Register your models here.
from .models import Product, Purchase, Cart

admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Cart)
