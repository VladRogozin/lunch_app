import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


@pytest.fixture
def api_client():
    # Така сама фікстура для створення клієнта API
    return APIClient()


@pytest.mark.django_db
def test_current_menu_view_unauthenticated(api_client):
    # Тест для перегляду поточного меню без аутентифікації
    # Відправляємо POST-запит до представлення без аутентифікації
    url = reverse('api/restaurants:current-menu')
    response = api_client.post(url, data={})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED