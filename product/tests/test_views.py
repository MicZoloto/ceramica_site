import pytest
from django.urls import reverse
from product.models import Category

@pytest.mark.django_db
def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_category_view(client):
    cat = Category.objects.create(name='Чашки', slug='chashky')
    url = reverse('category', args=[cat.slug])
    response = client.get(url)
    assert response.status_code == 200
    assert 'Чашки'.encode('utf-8') in response.content