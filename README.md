# Created for Quartely Meeting Summer 2019

## Repo Structure

### Web

This is an angular application that replicates a real world situation and uses NgRx and Redux patterns

### Test

This folder contains the selenium testing scripts for the frontend and application in general

### Models

This is an Django application that serves as the models representation of the database. It also contains the different API layers for each model following a CRUD model

### API

This is a Django application that serves as an API layer between the web and models layers. It combines endpoints and makes several requests to other functions to retrieve the data necessary

## API's Available

### Home

1. `http://localhost:8002/exp/home`
   - Type: GET
   - This endpoint retrieves the data needed for the home view on the angular app

### Food

1. `http://localhost:8001/api/foods/`
   - Type: GET
   - This endpoint retrieves the data about all foods

2. `http://localhost:8001/api/foods/<number>/`
   - Type: GET
   - This endpoint retrieves the data about a single food

### Drink

1. `http://localhost:8001/api/drinks/`
   - Type: GET
   - This endpoint retrieves the data about all drinks

2. `http://localhost:8001/api/drinks/<number>/`
   - Type: GET
   - This endpoint retrieves the data about a single drink
