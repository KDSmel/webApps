// src/app/models/alert.model.ts
export interface Alert {
  vehicle_id: string;
  timestamp: Date;
  alert_type: string;
  location: string;
  severity: string;
  camera_id: string;
}
