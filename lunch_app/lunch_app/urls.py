from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/restaurants/', include('lunch_api.urls')),
    path('api/users/', include('users.urls')),
    path('api/vote/', include('vote_api.urls')),
]
