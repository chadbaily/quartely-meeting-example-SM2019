import { EMPTY } from 'rxjs';
import { catchError, map, mergeMap, tap, withLatestFrom } from 'rxjs/operators';
import { Actions, Effect, ofType } from '@ngrx/effects';
import { Store, select } from '@ngrx/store';
import { Injectable } from '@angular/core';
import { AppState } from '../../store';
import * as fromSelenium from '../actions';

@Injectable()
export class SeleniumTestEffects {

  @Effect()
  attemptToLogin$ = this.actions$.pipe(
    ofType(fromSelenium.SeleniumTestAction.RequestToLogin),
    map(action => (<fromSelenium.RequestToLogin>action).payload),
    // mergeMap(payload => console.log('attempt to login'))
    tap(payload => console.log('test: ', payload))
  );
  constructor(private store: Store<AppState>, private actions$: Actions, ) { }
}