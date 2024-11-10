# /backend/scripts/anomaly_detection.py

from api.models.parking_data import ParkingData

def detect_anomaly(data):
    return data['available_spots'] < 5  # Trigger if available spots are below 5
