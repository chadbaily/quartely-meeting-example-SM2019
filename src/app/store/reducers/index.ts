import * as fromSelenium from '../actions';

export interface SeleniumTestState {
  isLoggedIn: boolean;
}

const INITIAL_STATE = {
  isLoggedIn: false
}

export function reducers(state: SeleniumTestState = INITIAL_STATE, action: fromSelenium.SeleniumTestActions): SeleniumTestState {
  switch (action.type) {

    case fromSelenium.SeleniumTestAction.RequestToLogin:
    return {...state};

    case fromSelenium.SeleniumTestAction.GrantLogin:
    return {...state, isLoggedIn: action.payload.value};

    default:
      return state;
  }
}