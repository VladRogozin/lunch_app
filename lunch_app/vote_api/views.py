from .models import Menu
from datetime import date

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from .serializers import VoteResultSerializer


class VoteResultView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = VoteResultSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        current_date = date.today()
        return queryset.filter(date=current_date)
