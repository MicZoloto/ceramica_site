import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_logout(client):
    user = User.objects.create_user(username='testuser', password='password')
    login_url = reverse('login')
    response = client.post(login_url, {'username': 'testuser', 'password': 'password'})
    assert response.status_code == 302  # redirect after login

    # Перевірка виходу
    logout_url = reverse('logout')
    response = client.get(logout_url)
    assert response.status_code == 302  # redirect after logout