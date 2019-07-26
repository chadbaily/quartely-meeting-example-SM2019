import { EMPTY } from 'rxjs';
import { catchError, map, mergeMap, tap, withLatestFrom } from 'rxjs/operators';
import { Actions, Effect, ofType } from '@ngrx/effects';
import { Store, select } from '@ngrx/store';
import { Injectable } from '@angular/core';
import { AppState } from '../../store';
import * as fromSelenium from '../actions';

@Injectable()
export class SeleniumTestEffects {

  @Effect({dispatch: false})
  attemptToLogin$ = this.actions$.pipe(
    ofType(fromSelenium.SeleniumTestAction.RequestToLogin),
    map(action => (<fromSelenium.RequestToLogin>action).payload),
    // mergeMap(payload => console.log('attempt to login'))
    tap(payload => console.log('test: ', payload))
  );

  // @Effect()
  //   requestToLoadHome$ = this.actions$.pipe(
  //   ofType(fromSelenium.SeleniumTestAction.RequestToLoadHome),
  //   tap(()) => this.store.dispatch(new))
  // );
  
  constructor(private store: Store<AppState>, private actions$: Actions, ) { }
}