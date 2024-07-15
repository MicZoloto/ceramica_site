"""
URL configuration for ceramica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from utils.sitemaps import CategorySitemap, PageSitemap
from debug_toolbar.toolbar import debug_toolbar_urls

sitemaps = {
    'category': CategorySitemap,
    'page': PageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('data/', include('data_import_export.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
] + debug_toolbar_urls()

handler404 = "product.views.page404"