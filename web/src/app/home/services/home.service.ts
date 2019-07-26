import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { take } from 'rxjs/operators';
import { HomePage } from 'src/app/types';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class HomeService {
  constructor(private httpClient: HttpClient) {}

  getHomePage(): Observable<HomePage | any> {
    // const api = this.httpClient.get('http://localhost:8002/exp/home/');
    const api = this.httpClient.get('./../../assets/home.json');
    console.log(
      api.subscribe(data => {
        return data;
      })
    );
    return api.pipe(take(1));
  }
}
