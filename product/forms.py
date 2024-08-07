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
        fields  = ['name', 'description_seo', 'keywords_seo', 'description', 'image']
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description_seo'].widget.attrs.update({'class': 'form-control'})
        self.fields['keywords_seo'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields  = ['name', 'description', 'description_seo', 'keywords_seo', 'category', 'image']
    def __init__(self, *args, **kwargs):
        super(SubCategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['description_seo'].widget.attrs.update({'class': 'form-control'})
        self.fields['keywords_seo'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

class PageForm(ModelForm):
    class Meta:
        model = Page
        fields  = ['title', 'slug', 'description_seo', 'keywords_seo', 'content']
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['description_seo'].widget.attrs.update({'class': 'form-control'})
        self.fields['keywords_seo'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше ім\'я', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Текст повідомлення', widget=forms.Textarea(attrs={'class': 'form-control'}))