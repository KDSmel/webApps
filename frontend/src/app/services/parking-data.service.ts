// src/app/services/parking-data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ParkingData } from '../models/parking-data.model';

@Injectable({
  providedIn: 'root'
})
export class ParkingDataService {
  private apiUrl = 'http://localhost:8000/api/parkingdata/';

  constructor(private http: HttpClient) {}

  getParkingData(): Observable<ParkingData[]> {
    return this.http.get<ParkingData[]>(this.apiUrl);
  }

  addAlert(parkingdata: ParkingData): Observable<ParkingData> {
    return this.http.post<ParkingData>(this.apiUrl, parkingdata);
  }
}
