from django.db.models import Avg
from rest_framework import serializers
from .models import Menu, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['employee', 'menu', 'point']


class VoteResultSerializer(serializers.ModelSerializer):
    average_point = serializers.SerializerMethodField()

    def get_average_point(self, obj):
        return obj.vote_set.aggregate(avg_point=Avg('point'))['avg_point']

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'average_point']
