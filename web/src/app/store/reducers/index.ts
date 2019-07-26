import * as fromSelenium from '../actions';
import { Message, Food } from 'src/app/types';

export interface SeleniumTestState {
  isLoggedIn: boolean;
  foods?: Food[]
}

const INITIAL_STATE = {
  isLoggedIn: false

};

export function reducers(
  state: SeleniumTestState = INITIAL_STATE,
  action: fromSelenium.SeleniumTestActions
): SeleniumTestState {
  switch (action.type) {

    case fromSelenium.SeleniumTestAction.RequestToLoadHome:
    case fromSelenium.SeleniumTestAction.RequestToLogin:
      return { ...state };

    case fromSelenium.SeleniumTestAction.GrantLogin:
      return {
        ...state,
        isLoggedIn: (<Message>action.payload).value === 'success'
      };

    case fromSelenium.SeleniumTestAction.LoadHome:
      return {...state, foods: action.payload}

    default:
      return state;
  }
}
