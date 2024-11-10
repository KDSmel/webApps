Sure, here are the step-by-step instructions to set up the front end of your Parking Security System using Angular:

### Step 1: Install Angular CLI
First, you need to install the Angular CLI globally on your machine if you haven't already.

```bash
npm install -g @angular/cli
```

### Step 2: Create a New Angular Project
Create a new Angular project named `parking-security-system-frontend`.

```bash
ng new parking-security-system-frontend
```

Navigate into the project directory:

```bash
cd parking-security-system-frontend
```

### Step 3: Generate Components, Services, and Models
Generate the necessary components, services, and models for your application.

#### Components
```bash
ng generate component components/alert-list
ng generate component components/camera-list
ng generate component components/parking-data
```

#### Services
```bash
ng generate service services/alert
ng generate service services/camera
ng generate service services/parking-data
```

#### Models
Create the models manually in the `src/app/models` directory.

```typescript
// src/app/models/alert.model.ts
export interface Alert {
  vehicle_id: string;
  timestamp: Date;
  alert_type: string;
  location: string;
  severity: string;
  camera_id: string;
}

// src/app/models/camera.model.ts
export interface Camera {
  camera_id: string;
  location: string;
  is_active: boolean;
  installation_date: Date;
  last_maintenance_date: Date;
}

// src/app/models/parking-data.model.ts
export interface ParkingData {
  parking_lot: string;
  available_spots: number;
  timestamp: Date;
}
```

### Step 4: Implement Services
Implement the services to interact with the backend API.

```typescript
// src/app/services/alert.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Alert } from '../models/alert.model';

@Injectable({
  providedIn: 'root'
})
export class AlertService {
  private apiUrl = 'http://localhost:800

0

/api/alerts/';

  constructor(private http: HttpClient) {}

  getAlerts(): Observable<Alert[]> {
    return this.http.get<Alert[]>(this.apiUrl);
  }

  addAlert(alert: Alert): Observable<Alert> {
    return this.http.post<Alert>(this.apiUrl, alert);
  }
}
```

Similarly, implement the `CameraService` and `ParkingDataService`.

### Step 5: Update App Module
Update the `AppModule` to include the necessary imports and declarations.

```typescript
// src/app/app.module.ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AlertListComponent } from './components/alert-list/alert-list.component';
import { CameraListComponent } from './components/camera-list/camera-list.component';
import { ParkingDataComponent } from './components/parking-data/parking-data.component';

@NgModule({
  declarations: [
    AppComponent,
    AlertListComponent,
    CameraListComponent,
    ParkingDataComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    provideHttpClient(withInterceptorsFromDi())
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

### Step 6: Implement Components
Implement the components to display data from the services.

```typescript
// src/app/components/alert-list/alert-list.component.ts
import { Component, OnInit } from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { Alert } from '../../models/alert.model';

@Component({
  selector: 'app-alert-list',
  templateUrl: './alert-list.component.html',
  styleUrls: ['./alert-list.component.scss']
})
export class AlertListComponent implements OnInit {
  alerts: Alert[] = [];

  constructor(private alertService: AlertService) {}

  ngOnInit(): void {
    this.alertService.getAlerts().subscribe((data: Alert[]) => {
      this.alerts = data;
    });
  }
}
```

Similarly, implement the `CameraListComponent` and `ParkingDataComponent`.

### Step 7: Configure Routing
Configure routing to navigate between different components.

```typescript
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
```

### Step 8: Run the Angular Application
Run the Angular application using the Angular CLI.

```bash
ng serve
```

Navigate to `http://localhost:4200` in your web browser to see the application in action.

### Summary
You have now set up the front end of your Parking Security System using Angular. The application includes components for displaying alerts, cameras, and parking data, services for interacting with the backend API, and routing for navigation.