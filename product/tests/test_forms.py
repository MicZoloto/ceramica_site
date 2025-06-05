from product.forms import ProductForm, CategoryForm
from product.models import Category, Producer, SubCategory

def test_product_form_valid():
    cat = Category.objects.create(name='Кераміка', slug='keramika')
    prod = Producer.objects.create(name='Test producer')
    sub = SubCategory.objects.create(name='Декор', category=cat, slug='dekor')
    form_data = {
        'name': 'Ваза',
        'sub_category': sub.id,
        'producer': prod.id,
        'price': 150,
        'article': 'A123'
    }
    form = ProductForm(data=form_data)
    assert form.is_valid()

def test_category_form_empty_invalid():
    form = CategoryForm(data={})
    assert not form.is_valid()