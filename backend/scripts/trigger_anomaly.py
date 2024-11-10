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

# Run periodically
asyncio.run(check_and_trigger_anomalies())
