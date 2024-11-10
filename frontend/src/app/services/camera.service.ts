// src/app/services/camera.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Camera } from '../models/camera.model';

@Injectable({
  providedIn: 'root'
})
export class CameraService {
  private apiUrl = 'http://localhost:8000/api/cameras/';

  constructor(private http: HttpClient) {}

  getCameras(): Observable<Camera[]> {
    return this.http.get<Camera[]>(this.apiUrl);
  }

  addCamera(camera: Camera): Observable<Camera> {
    return this.http.post<Camera>(this.apiUrl, camera);
  }
}