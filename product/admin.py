from django.contrib import admin
from .models import Product, Category, Producer, SubCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Producer)