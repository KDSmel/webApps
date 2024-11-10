# api/models/alert.py
from django.db import models

class Camera(models.Model):
    camera_id = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    installation_date = models.DateField()
    last_maintenance_date = models.DateField()

    def __str__(self):
        return f"Camera {self.camera_id} at {self.location}"

class Alert(models.Model):
    vehicle_id = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    alert_type = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    severity = models.CharField(max_length=10)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name='alerts')

    def __str__(self):
        return f"{self.vehicle_id} - {self.alert_type} at {self.location} ({self.severity})"