# backend/api/serializers.py
from rest_framework import serializers
from .models import Alert, Camera

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    camera = CameraSerializer(read_only=True)
    camera_id = serializers.PrimaryKeyRelatedField(queryset=Camera.objects.all(), source='camera')

    class Meta:
        model = Alert
        fields = '__all__'