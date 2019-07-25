import { Action } from '@ngrx/store';
import { Login, Message } from '../../types';

export enum SeleniumTestAction {
  RequestToLogin = 'Attempting to login',
  GrantLogin = 'Attempting to login',
}

export class RequestToLogin implements Action {
  readonly type = SeleniumTestAction.RequestToLogin;
  constructor(public readonly payload: Login) { }
}

export class GrantLogin implements Action {
  readonly type = SeleniumTestAction.GrantLogin;
  constructor(public readonly payload: Message) { }
}

export type SeleniumTestActions = | RequestToLogin
  | GrantLogin;