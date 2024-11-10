// src/app/components/parking-data/parking-data.component.ts
import { Component, OnInit } from '@angular/core';
import { ParkingDataService } from '../../services/parking-data.service';
import { ParkingData } from '../../models/parking-data.model';

@Component({
  selector: 'app-parking-data',
  templateUrl: './parking-data.component.html',
  styleUrls: ['./parking-data.component.scss']
})
export class ParkingDataComponent implements OnInit {
  parkingdata: ParkingData[] = [];

  constructor(private parkingdataService: ParkingDataService) {}

  ngOnInit(): void {
    this.parkingdataService.getParkingData().subscribe((data: ParkingData[]) => {
      this.parkingdata = data;
    });
  }
}