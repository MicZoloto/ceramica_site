from django.shortcuts import redirect, render
from product.models import SubCategory, Category, Page
from django.views.decorators.cache import cache_page
from django.core.cache import cache

def navigations(request):
    # Спроба отримати дані з кешу
    categoriesfornav = cache.get('categoriesfornav_list')
    
    # Якщо даних в кеші немає, отримуємо їх з бази даних
    if not categoriesfornav:
        categoriesfornav = Category.objects.prefetch_related('subcategories').all()
        # Зберігаємо дані в кеші на 5 хвилин
        cache.set('categoriesfornav_list', categoriesfornav, 60*5)
        
    # Створення контексту для шаблону
    context = {
        "categoriesfornav": categoriesfornav,
    }
    return context

def pages(request):
    pages = cache.get('pages_list')
    if not pages:
        pages = Page.objects.all().values('title', 'slug')
        cache.set('pages_list', pages, 60*5)

    context = {
        "pages": pages,
    }
    return (context)