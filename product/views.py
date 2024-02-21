from django.shortcuts import render
from .models import Product, Category, Producer, SubCategory

# Create your views here.

def index(request):
    product = Product.objects.all()
    all_category = Category.objects.all()
    produscer = Producer.objects.all()
    context = {
        "product": product,
        "all_category": all_category,
        "produscer": produscer,
    }
    return render(request, 'product/index.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug) # Отримання категорії за його унікальним ідентифікатором (primary key).
    sub_category = SubCategory.objects.filter(category=category)
    product = Product.objects.all()
    context = {
        "product": product,
        "category": category,
        "sub_category": sub_category,
    }
    return render(request, 'product/category.html', context)    
