from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from carros.api import viewsets as carrosviewsets


route = routers.DefaultRouter()

route.register(r'carros', carrosviewsets.CarrosViewSet, basename='Carros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
