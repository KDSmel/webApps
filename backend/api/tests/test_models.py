# backend/api/tests/test_models.py
from django.test import TestCase
from api.models import Alert
from django.utils import timezone

class AlertModelTestCase(TestCase):
    def setUp(self):
        self.alert = Alert.objects.create(
            vehicle_id="V123",
            timestamp=timezone.now(),
            alert_type="Unauthorized entry",
            location="Entrance A",
            severity="high"
        )

    def test_alert_creation(self):
        self.assertEqual(self.alert.vehicle_id, "V123")
        self.assertEqual(self.alert.alert_type, "Unauthorized entry")
        self.assertEqual(self.alert.location, "Entrance A")
        self.assertEqual(self.alert.severity, "high")
