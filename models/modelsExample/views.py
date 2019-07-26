from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# import django settings file
from django.conf import settings

# Other imports
import json
import requests

# Import models
from .models import *

def home(request):
    return render(request, 'home.html')