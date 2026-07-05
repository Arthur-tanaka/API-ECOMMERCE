from django.contrib import admin
from catalog.models import Cart, CartItem, Category, Brand, Product

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)