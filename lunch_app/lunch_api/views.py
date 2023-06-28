from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant
from .models import Menu
from .serializers import MenuSerializer
from .serializers import RestaurantSerializer
from datetime import date
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from vote_api.models import Vote
from vote_api.serializers import VoteSerializer


class RestaurantListCreateView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuListCreateView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CurrentMenuView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = VoteSerializer

    def get_object(self):
        current_date = date.today()

        try:
            menu = Menu.objects.get(date=current_date)
        except Menu.DoesNotExist:
            return None

        return menu

    def post(self, request, *args, **kwargs):
        # Отримуємо об'єкт меню за допомогою методу get_object
        menu = self.get_object()
        if not menu:
            # Якщо об'єкт меню не існує, повертаємо помилку 404 Not Found
            return Response({'detail': 'No menu available for today.'}, status=status.HTTP_404_NOT_FOUND)

        # Отримуємо об'єкт співробітника, пов'язаний з поточним користувачем
        employee = request.user.employee
        if not employee:
            # Якщо об'єкт співробітника не знайдено, повертаємо помилку 400 Bad Request
            return Response({'detail': 'No employee found for the user.'}, status=status.HTTP_400_BAD_REQUEST)

        # Перевіряємо, чи співробітник вже голосував за меню поточного дня
        if Vote.objects.filter(employee=employee, menu=menu).exists():
            # Якщо голосування вже існує, повертаємо помилку 400 Bad Request
            return Response({'detail': 'Employee has already voted for today\'s menu.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Ініціалізуємо серіалізатор з даними з запиту
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Зберігаємо голосування, встановлюючи співробітника та меню
        serializer.save(employee=employee, menu=menu)

        # Повертаємо відповідь з успішним повідомленням
        return Response({'detail': 'Vote recorded successfully.'}, status=status.HTTP_201_CREATED)
