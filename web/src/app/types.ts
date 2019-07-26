export interface Login {
  username: string;
  password: string;
}

export interface Message {
  value: string;
}

export interface Food {
  pk: number;
  name: string;
  description: string;
  price: number;
  quanity: number;
}

export interface Drink {
  pk: number;
  name: string;
  description: string;
  price: number;
  quanity: number;
}

export interface HomePage {
  food: Food[];
  drink: Drink[]
}