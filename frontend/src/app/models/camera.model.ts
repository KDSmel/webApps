// src/app/models/camera.model.ts
export interface Camera {
  camera_id: string;
  location: string;
  is_active: boolean;
  installation_date: Date;
  last_maintenance_date: Date;
}