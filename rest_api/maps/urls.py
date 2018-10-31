from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('maps', views.MapsView)


urlpatterns = [
   path('', include(router.urls))
    
]