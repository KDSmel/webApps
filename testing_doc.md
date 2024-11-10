Here’s how to proceed with adding sample data to MongoDB and setting up unit and integration tests for your solution.

### Step 1: Add Sample Data to MongoDB

#### 1.1 Create Sample Data Script
To add sample data to MongoDB, create a Python script that inserts predefined entries into your collections.

```python
# backend/scripts/add_sample_data.py
from pymongo import MongoClient
from datetime import datetime

# Set up MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client['parking_security_db']

# Sample data for the `alerts` collection
sample_alerts = [
    {
        "vehicle_id": "V123",
        "timestamp": datetime.now(),
        "alert_type": "Unauthorized entry",
        "location": "Entrance A",
        "severity": "high",
    },
    {
        "vehicle_id": "V124",
        "timestamp": datetime.now(),
        "alert_type": "Suspicious movement",
        "location": "Zone B",
        "severity": "medium",
    },
]

# Insert sample data
def add_sample_data():
    db.alerts.insert_many(sample_alerts)
    print("Sample data added to the database.")

if __name__ == "__main__":
    add_sample_data()
```

#### 1.2 Run the Script
Run the script from the terminal to populate your database with the sample data.

```bash
python backend/scripts/add_sample_data.py
```

---

### Step 2: Setting Up Unit and Integration Tests

#### 2.1 Unit Tests

To set up unit tests, create a `tests` directory within the `api` app and add a script to test each model, view, or utility function. Here’s an example of testing your models and view functions.

Create a test file for models in `api/tests/test_models.py`:

```python
# backend/api/tests/test_models.py
from django.test import TestCase
from api.models import Alert
from datetime import datetime

class AlertModelTestCase(TestCase):
    def setUp(self):
        self.alert = Alert.objects.create(
            vehicle_id="V123",
            timestamp=datetime.now(),
            alert_type="Unauthorized entry",
            location="Entrance A",
            severity="high"
        )

    def test_alert_creation(self):
        self.assertEqual(self.alert.vehicle_id, "V123")
        self.assertEqual(self.alert.alert_type, "Unauthorized entry")
        self.assertEqual(self.alert.location, "Entrance A")
        self.assertEqual(self.alert.severity, "high")
```

#### 2.2 Integration Tests

Integration tests will test the full data flow in your app. Here’s an example of how to write an integration test to verify API functionality.

Create a file `backend/api/tests/test_views.py` to test the API endpoint:

```python
# backend/api/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Alert
from datetime import datetime

class AlertViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Alert.objects.create(
            vehicle_id="V123",
            timestamp=datetime.now(),
            alert_type="Unauthorized entry",
            location="Entrance A",
            severity="high"
        )

    def test_get_alerts(self):
        response = self.client.get(reverse('alert-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
```

#### 2.3 Running Tests

Run all tests with Django’s testing framework by running:

```bash
python manage.py test api
```

This setup provides a structured approach to populate your MongoDB with sample data and verify core functionalities through unit and integration testing.
