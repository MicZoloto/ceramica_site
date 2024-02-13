from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField('Назва товару', max_length=200, null=True, blank=True)
    #category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    #producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField('Ціна товару', null=True, blank=True)
    image = models.ImageField('Зображення товару ', null=True, blank=True, default='default.png')
    article = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('Дата публікації', auto_now_add=True)

    def __str__(self):
        return f"{self.title} / {self.category} / {self.producer}"
    
    class Meta:
        verbose_name = "Виріб"
        verbose_name_plural = "Вироби"
    
    