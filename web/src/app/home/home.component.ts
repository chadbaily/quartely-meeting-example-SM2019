import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState, selectFoods } from '../store';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  foods$ = this.store.select(state => selectFoods(state));
  constructor(private store: Store<AppState>, private titleService: Title) {}

  ngOnInit() {
    this.titleService.setTitle('Home');
  }
}
