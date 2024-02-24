from django.shortcuts import redirect, render
from product.models import Category, SubCategory

def navigations(request):
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {
        "cat_nav": category,
        "sub_cat_nav": sub_category,
    }
    return (context)