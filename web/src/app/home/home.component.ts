import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState, selectHomePageContent } from '../store';
import { Title } from '@angular/platform-browser';

import * as fromSelenium from '../store/actions';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  homePageContent$ = this.store.select(state => selectHomePageContent(state));
  constructor(private store: Store<AppState>, private titleService: Title) {
    this.store.dispatch(new fromSelenium.RequestToLoadHome());
  }

  ngOnInit() {
    this.titleService.setTitle('Home');
  }
}
