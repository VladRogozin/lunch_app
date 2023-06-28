from django.urls import path
from .views import VoteResultView


app_name = 'api/vote'

urlpatterns = [
    path('vote-results/', VoteResultView.as_view(), name='vote-results'),
]
