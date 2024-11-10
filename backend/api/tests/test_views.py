# backend/api/tests/test_views.py
# api/tests/test_views.py
# api/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Alert
from django.utils import timezone


class AlertViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create an alert in the test database
        Alert.objects.create(
            vehicle_id="V123",
            timestamp=timezone.now(),
            alert_type="Unauthorized entry",
            location="Entrance A",
            severity="high"
        )

    def test_get_alerts(self):
        # Use the correct URL pattern name
        response = self.client.get(reverse('alert-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

