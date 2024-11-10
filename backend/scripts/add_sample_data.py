# backend/scripts/add_sample_data.py
from pymongo import MongoClient
from datetime import datetime

# Set up MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client['parking_security_db']

# Sample data for the `cameras` collection
sample_cameras = [
    {
        "camera_id": "C001",
        "location": "Entrance A",
        "is_active": True,
        "installation_date": datetime(2021, 5, 20),
        "last_maintenance_date": datetime(2023, 1, 15),
    },
    {
        "camera_id": "C002",
        "location": "Zone B",
        "is_active": False,
        "installation_date": datetime(2020, 8, 10),
        "last_maintenance_date": datetime(2022, 11, 5),
    },
]

# Sample data for the `alerts` collection
sample_alerts = [
    {
        "vehicle_id": "V123",
        "timestamp": datetime.now(),
        "alert_type": "Unauthorized entry",
        "location": "Entrance A",
        "severity": "high",
        "camera_id": "C001",
    },
    {
        "vehicle_id": "V124",
        "timestamp": datetime.now(),
        "alert_type": "Suspicious movement",
        "location": "Zone B",
        "severity": "medium",
        "camera_id": "C002",
    },
]

# Insert sample data
def add_sample_data():
    db.cameras.insert_many(sample_cameras)
    db.alerts.insert_many(sample_alerts)
    print("Sample data added to the database.")

if __name__ == "__main__":
    add_sample_data()