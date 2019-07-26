from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt


# Other imports
import json
import requests

# Create your views here.


def home(request):
    # Call the models layer to get the foods
    food_list = requests.get('http://models-api:8000/api/foods/')
    # print(food_list)
    food_list = json.loads((food_list.text))
    foods = food_list['result']
    # print(foods)

    # Call the models layer to get the drinks
    drink_list = requests.get('http://models-api:8000/api/drinks/')
    # print(drink_list)
    drink_list = json.loads((drink_list.text))
    drinks = drink_list['result']

    data = {
        "food": foods,
        "drink": drinks
    }
    # Return the json of foods
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')
