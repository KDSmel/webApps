import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParkingDataComponent } from './parking-data.component';

describe('ParkingDataComponent', () => {
  let component: ParkingDataComponent;
  let fixture: ComponentFixture<ParkingDataComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ParkingDataComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ParkingDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
