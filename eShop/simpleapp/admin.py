from django.contrib import admin
from .models import Category, Material, Product, ProductMaterial


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(ProductMaterial)
