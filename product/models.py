from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.

class Product(models.Model):
    name = models.CharField('Назва товару', max_length=200, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField('Ціна товару', null=True, blank=True)
    image = models.ImageField('Зображення товару ', null=True, blank=True, default='default.png')
    article = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return f"{self.name} / {self.category} / {self.producer}"
    
    class Meta:
        verbose_name = "Виріб"
        verbose_name_plural = "Вироби"

    
class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)
    slug = models.SlugField('Назва для ЧПУ', unique=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} / {self.pub_date}"
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        slug_text = unidecode(self.name)
        self.slug = slugify(slug_text)
        super().save(*args, **kwargs)


class Producer(models.Model):
    name = models.CharField('Назва виробника',max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return f"{self.name} / {self.pub_date}"
    
    class Meta:
        verbose_name = "Виробник"
        verbose_name_plural = "Виробники"