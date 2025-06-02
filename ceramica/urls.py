from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from utils.sitemaps import CategorySitemap, PageSitemap, SubCategorySitemap
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static

sitemaps = {
    'category': CategorySitemap,
    'subcategory': SubCategorySitemap,
    'page': PageSitemap,    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('data/', include('data_import_export.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
] + debug_toolbar_urls()

handler404 = "product.views.page404"

# Для роздачі media файлів у dev
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)