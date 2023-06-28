import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    # Фікстура для створення клієнта API
    return APIClient()


@pytest.fixture
def create_user():
    def make_user(username, password):
        # Функція для створення користувача
        return User.objects.create_user(username=username, password=password)

    return make_user


@pytest.mark.django_db
def test_create_user(api_client):
    # Тест для створення користувача

    user_data = {
        'username': 'testuser',
        'password': 'testpassword',
    }
    # Виконуємо POST-запит на створення користувача
    response = api_client.post('/api/users/users/', data=user_data)

    assert response.status_code == 201
    assert User.objects.filter(username='testuser').exists()
