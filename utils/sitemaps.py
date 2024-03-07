from django.contrib import sitemaps
from django.urls import reverse
from product.models import Category, Page

class CategorySitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse('category', args=[item.slug])

    def __iter__(self):
        for item in self.items():
            yield item

class PageSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Page.objects.all()

    def location(self, item):
        return reverse('page', args=[item.slug])

    def __iter__(self):
        for item in self.items():
            yield item