from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    votes = serializers.SerializerMethodField()

    def get_votes(self, obj):
        return obj.vote_set.count()  # Отримуємо загальну кількість голосів для даного меню

    class Meta:
        model = Menu
        fields = '__all__'
