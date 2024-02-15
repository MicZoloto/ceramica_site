from django.shortcuts import render
from .models import Product, Category, Producer

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