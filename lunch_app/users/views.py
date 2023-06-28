from .serializers import EmployeeSerializer
from .serializers import MyTokenObtainPairSerializer
from .serializers import UserSerializer
from .models import Employee
from django.contrib.auth.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ObtainTokenPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
