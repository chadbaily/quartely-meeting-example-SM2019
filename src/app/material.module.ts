import { NgModule } from '@angular/core';
import { MatButtonModule, MatCheckboxModule, MatCardModule, MatInputModule } from '@angular/material';

@NgModule({
  imports: [MatButtonModule, MatCheckboxModule, MatCardModule, MatInputModule],
  exports: [MatButtonModule, MatCheckboxModule, MatCardModule, MatInputModule],
})
export class MaterialModule { }