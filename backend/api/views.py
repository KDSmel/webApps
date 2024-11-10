from django.shortcuts import render

# /backend/api/views.py

from rest_framework import viewsets
from .models import Camera, Alert
from .serializers import CameraSerializer,AlertSerializer  # You must also create a serializer for your model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.parking_data import ParkingData

@api_view(['GET'])
def get_parking_data(request):
    data = ParkingData.objects.order_by('-timestamp').first()
    return Response(data.to_dict() if data else {})

@api_view(['POST'])
def add_parking_data(request):
    parking_lot = request.data.get('parking_lot')
    available_spots = request.data.get('available_spots')
    parking_data = ParkingData(parking_lot=parking_lot, available_spots=available_spots)
    parking_data.save()
    return Response(parking_data.to_dict(), status=201)


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

