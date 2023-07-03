from django.contrib import admin
from .models import Product,Product_accessories,Product_Alternative,Category

admin.site.register(Product)
admin.site.register(Product_accessories)
admin.site.register(Product_Alternative)
admin.site.register(Category)