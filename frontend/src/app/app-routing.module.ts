// src/app/app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AlertListComponent } from './components/alert-list/alert-list.component';
import { CameraListComponent } from './components/camera-list/camera-list.component';
import { ParkingDataComponent } from './components/parking-data/parking-data.component';

const routes: Routes = [
  { path: 'alerts', component: AlertListComponent },
  { path: 'cameras', component: CameraListComponent },
  { path: 'parking-data', component: ParkingDataComponent },
  { path: '', redirectTo: '/alerts', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }