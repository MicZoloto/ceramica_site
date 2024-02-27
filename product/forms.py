from django.forms import ModelForm, widgets
from .models import Product, Category, Producer, SubCategory, Page
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields  = ['name', 'sub_category', 'producer', 'price', 'image', 'article']
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
        fields  = ['name', 'description', 'image']
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields  = ['name', 'description', 'category']
    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields  = ['title', 'slug', 'content']
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})