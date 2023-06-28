from django.urls import path
from .views import ObtainTokenPairView, UserCreateView
from .views import EmployeeListCreateView


app_name = 'api/users'

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
]
