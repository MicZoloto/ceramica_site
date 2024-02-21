from django.forms import ModelForm, widgets
from .models import Product, Category, Producer, SubCategory
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields  = ['name', 'sub_category', 'producer', 'price', 'image', 'article']
        '''widgets = {
            'full_text': TinyMCE(attrs={'cols': 50, 'rows': 30}),
        }
'''
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['sub_category'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['producer'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-select'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['article'].widget.attrs.update({'class': 'form-control'})


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields  = ['name', 'image']
        '''widgets = {
            'full_text': TinyMCE(attrs={'cols': 50, 'rows': 30}),
        }
'''
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})