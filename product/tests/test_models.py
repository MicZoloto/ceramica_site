import pytest
from product.models import Category, SubCategory, Producer, Product

@pytest.mark.django_db
def test_category_str():
    cat = Category.objects.create(name='Тест', slug='test')
    assert str(cat).startswith('Тест')

@pytest.mark.django_db
def test_subcategory_foreign_key():
    cat = Category.objects.create(name='Тест', slug='test')
    sub = SubCategory.objects.create(name='Підкатегорія', category=cat, slug='sub-test')
    assert sub.category == cat