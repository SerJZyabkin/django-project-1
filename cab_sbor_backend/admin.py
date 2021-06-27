from django.contrib import admin
from .models import NewsEntry, ProductGroupEntry, Product, ProductCategory
# Register your models here.

admin.site.register(NewsEntry)
admin.site.register(ProductGroupEntry)
# admin.site.register(Product)
# admin.site.register(ProductCategory)