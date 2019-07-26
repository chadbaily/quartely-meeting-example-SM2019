import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from '../store';
import { Login } from '../types';
import * as fromSelenium from '../store/actions';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  constructor(private store: Store<AppState>, private titleService: Title) {}

  ngOnInit() {
    this.titleService.setTitle('Login');
  }

  submit() {
    console.log('did a thing');
    const temp: Login = {
      username: 'test',
      password: '1234234'
    };
    this.store.dispatch(new fromSelenium.RequestToLogin(temp));
  }
}
