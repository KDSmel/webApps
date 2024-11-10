# /backend/api/models/parking_data.py

from mongoengine import Document, StringField, IntField, DateTimeField
from datetime import datetime

class ParkingData(Document):
    parking_lot = StringField(required=True)
    available_spots = IntField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)

    def to_dict(self):
        return {
            'parking_lot': self.parking_lot,
            'available_spots': self.available_spots,
            'timestamp': self.timestamp,
        }
