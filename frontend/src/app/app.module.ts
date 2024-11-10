// src/app/app.module.ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AlertListComponent } from './components/alert-list/alert-list.component';
import { CameraListComponent } from './components/camera-list/camera-list.component';
import { ParkingDataComponent } from './components/parking-data/parking-data.component';
import { AlertService } from './services/alert.service';

@NgModule({
  declarations: [
    AppComponent,
    AlertListComponent,
    CameraListComponent,
    ParkingDataComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [AlertService],
  bootstrap: [AppComponent]
})
export class AppModule { }