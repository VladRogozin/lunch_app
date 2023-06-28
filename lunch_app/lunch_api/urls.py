from django.urls import path
from .views import RestaurantListCreateView
from .views import MenuListCreateView
from .views import CurrentMenuView


app_name = 'api/restaurants'

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('menus/', MenuListCreateView.as_view(), name='menu-list-create'),
    path('current-menu/', CurrentMenuView.as_view(), name='current-menu'),
]
