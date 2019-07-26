import { Action } from '@ngrx/store';
import { Login, Message, Food, HomePage } from '../../types';

export enum SeleniumTestAction {
  RequestToLogin = 'Attempting to login',
  GrantLogin = 'Attempting to login',
  RequestToLoadHome = 'Requesting to load home page content',
  LoadHome = 'Loading home page content'
}

export class RequestToLogin implements Action {
  readonly type = SeleniumTestAction.RequestToLogin;
  constructor(public readonly payload: Login) {}
}

export class GrantLogin implements Action {
  readonly type = SeleniumTestAction.GrantLogin;
  constructor(public readonly payload: Message) {}
}

export class RequestToLoadHome implements Action {
  readonly type = SeleniumTestAction.RequestToLoadHome;
}

export class LoadHome implements Action {
  readonly type = SeleniumTestAction.LoadHome;
  constructor(public readonly payload: HomePage) {}
}

export type SeleniumTestActions =
  | RequestToLogin
  | GrantLogin
  | RequestToLoadHome
  | LoadHome;
