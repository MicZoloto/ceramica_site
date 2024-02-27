from django.shortcuts import redirect, render
from product.models import Category, SubCategory, Page

def navigations(request):
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {
        "cat_nav": category,
        "sub_cat_nav": sub_category,
    }
    return (context)

def pages(request):
    top_nav = Page.objects.all()

    context = {
        "top_nav": top_nav,
    }
    return (context)