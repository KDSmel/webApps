Let's build a **Parking Security System** backend using **Django** with **MongoDB** integration for data storage, WebSocket support for real-time alerts, and a modular structure with API endpoints, database models, and anomaly detection scripts. We'll also use **Django Channels** for WebSocket management. The MongoDB configuration will include a sample database setup.

---

### Step-by-Step Guide to Building the Backend
### Folder Structure
The project structure will look like this:
```
ParkingSecuritySystem
├── backend
│   ├── api
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── websocket
│   │   │   ├── __init__.py
│   │   │   └── consumers.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── test_models.py
│   │   │   └── test_views.py
│   ├── scripts
│   │   ├── __init__.py
│   │   ├── add_sample_data.py
│   │   ├── anomaly_detection.py
│   │   └── trigger_anomaly.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
├── README.md
├── readmesummary.md
├── testing_doc.md
```
### Explanation of Project Files

#### Main Project Directory
- **README.md**: Main project documentation providing an overview and setup instructions.
- **readmesummary.md**: Summary of the project setup and configuration.
- **testing_doc.md**: Documentation for setting up and running tests.

#### Backend Directory
- **config**: The main Django project directory containing project-wide settings and configurations.
  - **__init__.py**: Initializes the backend module.
  - **asgi.py**: ASGI configuration for WebSocket support.
  - **settings.py**: Django project settings, including database configurations, installed apps, middleware, etc.
  - **urls.py**: Main URL configuration for the project, including routes to the API and admin site.
  - **wsgi.py**: WSGI configuration for deployment.

#### API Directory
- **api**: The Django app for handling API endpoints and WebSocket consumers.
  - **__init__.py**: Initializes the API module.
  - **models.py**: Defines the database models for the application.
  - **serializers.py**: Defines the serializers for converting model instances to and from JSON.
  - **urls.py**: Defines the URL routes for the API.
  - **views.py**: Defines the views for handling API requests.
  - **websocket**: Contains WebSocket consumer definitions.
    - **__init__.py**: Initializes the websocket module.
    - **consumers.py**: Defines the WebSocket consumers for handling real-time communication.
  - **tests**: Contains unit and integration tests.
    - **__init__.py**: Initializes the tests module.
    - **test_models.py**: Tests for the models.
    - **test_views.py**: Tests for the views.

#### Scripts Directory
- **scripts**: Contains scripts for various tasks.
  - **__init__.py**: Initializes the scripts module.
  - **add_sample_data.py**: Script to add sample data to the database.
  - **anomaly_detection.py**: Script for anomaly detection.
  - **trigger_anomaly.py**: Script to trigger anomaly alerts.

#### Management Script
- **manage.py**: Django management script for running commands such as `runserver`, `migrate`, and `createsuperuser`.

This structure provides a clear organization of the project components, making it easier to navigate and maintain.

### Step 1: Set Up the Django Project

1. **Create and Activate a Virtual Environment**:
   ```bash
   mkdir parking-security-system
   cd parking-security-system
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install Django and Required Packages**:
   ```bash
   pip install django djangorestframework channels channels_redis pymongo mongoengine
   ```

3. **Create the Django Project**:
   ```bash
   django-admin startproject backend .
   cd backend
   django-admin startapp api
   ```

### Step 2: Configure Django Project Settings

Open `backend/settings.py` and make the following changes to configure MongoDB and Django Channels:

#### Add Installed Apps

```python
# backend/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',            # Django REST Framework
    'channels',                  # WebSocket support
    'api',                       # Our app for API and WebSocket handling
]
```

#### MongoDB Configuration

Use `mongoengine` to connect Django to MongoDB:

```python
# backend/settings.py

# MongoDB Configuration
from mongoengine import connect
connect('parking_security_db', host='mongodb://localhost:27017/parking_security_db')
```

#### Django Channels and WebSocket Configuration

Add configuration for Django Channels and WebSocket with Redis as the channel layer:

```python
# backend/settings.py

ASGI_APPLICATION = 'backend.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

---

### Step 3: Set Up Database Models

Create the MongoDB database model in `models.py`.

1. **Define ParkingData Model in MongoDB**

Create the `/api/models/parking_data.py` file and define the `ParkingData` model.

```python
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
```

### Step 4: Create API Views for Data Access

Define REST API endpoints for getting and posting parking data.

1. **Define Views in `views.py`**

Add these views to allow adding and retrieving parking data.

```python
# /backend/api/views.py

from django.shortcuts import render
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
```

2. **Define URLs for API Endpoints**

In `api/urls.py`, define the routes for the API.
```python
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
```

In `backend/urls.py`, include the `api` app’s URLs:
```python
# /backend/backend/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the URLs from the api app
]
```

### Step 5: Set Up WebSocket for Real-Time Alerts

1. **WebSocket Consumer for Alerts**

Define the WebSocket consumer in `api/websocket/consumers.py`.

```python
# /backend/api/websocket/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'parking_alerts'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.send(text_data=json.dumps({'message': message}))

    async def send_alert(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
```

2. **Define ASGI Configuration**

Update the `backend/asgi.py` to route WebSocket connections to the `AlertConsumer`.

```python
# /backend/backend/asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from api.websocket import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/alerts/", consumers.AlertConsumer.as_asgi()),
        ])
    ),
})
```

### Step 6: Implement Anomaly Detection Script

Create a script that checks for low parking spots and sends alerts.

1. **Define Anomaly Detection Script**

In `scripts/anomaly_detection.py`, implement anomaly detection.

```python
# /backend/scripts/anomaly_detection.py

from api.models.parking_data import ParkingData

def detect_anomaly(data):
    return data['available_spots'] < 5  # Trigger if available spots are below 5
```

2. **Script to Trigger Anomaly Alert**

In `/scripts/trigger_anomaly.py`, check data and send WebSocket alerts.

```python
# /backend/scripts/trigger_anomaly.py

import json
import asyncio
from channels.layers import get_channel_layer
from .anomaly_detection import detect_anomaly
from api.models.parking_data import ParkingData

async def check_and_trigger_anomalies():
    data = ParkingData.objects.order_by('-timestamp').first()
    if data and detect_anomaly(data.to_dict()):
        alert_message = "Low parking spots detected!"
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            'parking_alerts',
            {
                'type': 'send_alert',
                'message': alert_message
            }
        )
```
3. **Script to Convert Alerts from and to JSON** 
/api/serializers.py
Script to handle the conversion of Alert and Camera model instances to and from JSON, making it easier to work with these objects in a web API context.
```python
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
```


4. **Script to define the alert content** 
Script providing a human-readable representation of the Alert with the fields to include
\api\models\alert.py

```python
# api/models/alert.py
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

```

# Run periodically
asyncio.run(check_and_trigger_anomalies())
```

### Step 7: Run the Project

1. **Start Redis for Channels**:
   Ensure Redis is running locally for Channels.

2. **Run Django Server**:
   ```bash
   python manage.py runserver
   ```

3. **Monitor Anomalies**:
   Run the anomaly detection script in the background:
   ```bash
   python scripts/trigger_anomaly.py
   ```

---

### MongoDB Sample Data

To add sample data to MongoDB, run:

```python
# /backend/scripts/add_sample_data.py

from api.models.parking_data import ParkingData

# Add sample data
sample_data = [
    {"parking_lot": "Lot A", "available_spots": 10},
    {"parking_lot": "Lot B", "available_spots": 2},
]

for data in sample_data:
    parking_data = ParkingData(**data)
    parking_data.save()
    print(f"Added data for {data['parking_lot']}")
```

---

This setup provides a fully functional Django backend with MongoDB integration, REST API, WebSocket alert system, and a periodic anomaly detection script for real-time alerts in a **Parking Security System**.
