from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.

class Product(models.Model):
    name = models.CharField('Назва товару', max_length=200, null=True, blank=True)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Розділ')
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Виробник')
    price = models.IntegerField('Ціна товару', null=True, blank=True)
    image = models.ImageField('Зображення товару ', null=True, blank=True, default='default.jpg')
    article = models.CharField('Артікль', max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return f"{self.name} / {self.sub_category} / {self.producer.name}"
    
    class Meta:
        verbose_name = "Виріб"
        verbose_name_plural = "Вироби"

    
class Category(models.Model):
    name = models.CharField('Назва категорії', max_length=200, null=True, blank=True)
    description = models.TextField('Опис', null=True, blank=True)

    description_seo = models.CharField(max_length=255, verbose_name='Опис для SEO', blank=True)
    keywords_seo = models.CharField(max_length=255, verbose_name='Ключові слова для SEO', blank=True)

    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)
    slug = models.SlugField('Назва для ЧПУ', unique=True, null=True, blank=True)
    image = models.ImageField('Зображення для розділу ', null=True, blank=True, default='default.jpg')

    def __str__(self):
        return f"{self.name} / {self.pub_date}"
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        slug_text = unidecode(self.name)
        self.slug = slugify(slug_text)

        if not self.description:
            self.description = self.title

        super().save(*args, **kwargs)

class SubCategory(models.Model):
    name = models.CharField('Назва підкатегоії', max_length=200, null=True, blank=True)
    description = models.TextField('Опис', null=True, blank=True)

    description_seo = models.CharField(max_length=255, verbose_name='Опис для SEO', blank=True)
    keywords_seo = models.CharField(max_length=255, verbose_name='Ключові слова для SEO', blank=True)

    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)
    slug = models.SlugField('Назва для ЧПУ', unique=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField('Зображення для підрозділу ', null=True, blank=True, default='default.jpg')

    def __str__(self):
        return f"{self.name} / {self.pub_date}"
    
    class Meta:
        verbose_name = "Підкатегорія"
        verbose_name_plural = "Підкатегорії"

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

class Page(models.Model):
    title = models.CharField('Загловок сторінки', max_length=100, null=True, blank=True)
    slug = models.SlugField('Назва для ЧПУ', unique=True, null=True, blank=True)

    description_seo = models.CharField(max_length=255, verbose_name='Опис для SEO', blank=True)
    keywords_seo = models.CharField(max_length=255, verbose_name='Ключові слова для SEO', blank=True)

    content = models.TextField('Оcновна інформація', null=True, blank=True)
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return f"{self.title} / {self.pub_date}"
    
    class Meta:
        verbose_name = "Сторінка"
        verbose_name_plural = "Сторінки"

    def save(self, *args, **kwargs):
        if not self.slug:  # перевірка чи slug порожній
            slug_text = unidecode(self.title)
            self.slug = slugify(slug_text)
        if not self.description_seo:
            self.description_seo = self.title
        super().save(*args, **kwargs)