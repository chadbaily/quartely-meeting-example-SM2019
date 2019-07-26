import {
  ActionReducerMap,
  createFeatureSelector,
  createSelector
} from '@ngrx/store';

import * as fromSelenium from './reducers';

export interface AppState {
  store: fromSelenium.SeleniumTestState;
}

export const reducers: ActionReducerMap<AppState> = {
  store: fromSelenium.reducers
};

const getSeleniumTest = createFeatureSelector<
  AppState,
  fromSelenium.SeleniumTestState
>('store');

export const selectIsLoggedIn = createSelector(
  getSeleniumTest,
  (state: fromSelenium.SeleniumTestState) => state.isLoggedIn
);
export const selectHomePageContent = createSelector(
  getSeleniumTest,
  (state: fromSelenium.SeleniumTestState) => state.homeContent
);
