// src/app/components/camera-list/camera-list.component.ts
import { Component, OnInit } from '@angular/core';
import { CameraService } from '../../services/camera.service';
import { Camera } from '../../models/camera.model';

@Component({
  selector: 'app-camera-list',
  templateUrl: './camera-list.component.html',
  styleUrls: ['./camera-list.component.scss']
})
export class CameraListComponent implements OnInit {
  cameras: Camera[] = [];

  constructor(private cameraService: CameraService) {}

  ngOnInit(): void {
    this.cameraService.getCameras().subscribe((data: Camera[]) => {
      this.cameras = data;
    });
  }
}