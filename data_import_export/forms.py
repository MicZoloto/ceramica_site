from django.forms import ModelForm, widgets
from product.models import Product, Category, Producer, SubCategory, Page
from django import forms

class ExportCsvForm(forms.Form):
    """Форма для експорту CSV-файлу"""
    sub_categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=SubCategory.objects.all().values_list('id', 'name')
    )

    def get_products(self):
        """Отримання товарів для експорту"""
        sub_categories = self.cleaned_data['sub_categories']
        products = Product.objects.filter(sub_category__in=sub_categories)
        return products

class ImportCsvForm(forms.Form):
    csv_file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 
                                                             'id': 'inputGroupFile04',
                                                             'aria-describedby':'inputGroupFileAddon03',
                                                             'aria-label':'Upload',
                                                             }))
