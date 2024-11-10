# /backend/api/urls.py
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CameraViewSet, AlertViewSet # Import your viewset

router = DefaultRouter()
router.register(r'cameras', CameraViewSet, basename='camera')
router.register(r'alerts', AlertViewSet, basename='alert')

urlpatterns = [
    path('api/', include(router.urls)),  # Include the router URLs
    path('api/parking-data/', views.get_parking_data),
    path('api/parking-data/add/', views.add_parking_data),
]

