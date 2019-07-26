# First external includes
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseRedirect, HttpResponse

# other
import json

# Authenticator
import os
import hmac
import datetime
# import django settings file
from django.conf import settings

# Import Models
from .models import *

# Import serializer
from .serializers import *

# Import all responses needed
from .responses import *

class FoodViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    model = Food

    '''
    __________________________________________________  Delete
     url: DELETE : <WEBSITE>/api/foods/pk
     function: Deletes a food item
    __________________________________________________
    '''

    def delete(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                result.delete()
            except self.model.DoesNotExist:
                return object_not_found_response()
            except IntegrityError:
                return object_is_foreign_key_response()

            return successful_delete_response()

    '''
    __________________________________________________  get
     url: GET : <WEBSITE>/api/foods/
     function: Returns list of all foods

     url: GET : <WEBSITE>/api/foods/pk
     function: returns details on one food
    __________________________________________________
    '''

    def get(self, request, format=None, pk=None):
        # print(pk)
        is_many = True
        if pk is None:
            result = self.model.objects.all()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                # print(result)
                is_many = False
            except self.model.DoesNotExist:
                return object_not_found_response()

        serializer = self.serializer_class(result, many=is_many)
        return successful_create_response(serializer.data)

    '''
    __________________________________________________  Post
     url: POST : <WEBSITE>/api/foods/
     Body:
     {
     "food": {
        "seller": 1,
        "name": "Beluga Caviar",
        "description": "velvety, salty, briny, little black pearls of delish",
        "price": 100.0
    }
    }
    function: Creates a seller and user. Associates user to seller
    __________________________________________________
    '''

    def post(self, request, format=None, pk=None):
        if pk is None:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_create_response(serializer.data)
        else:
            return colliding_id_response()

    '''
    __________________________________________________  Put
     url: PUT : <WEBSITE>/api/foods/pk
     function: Updates a food item
    __________________________________________________
    '''

    def put(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return object_not_found_response()

            serializer = self.serializer_class(result, data=request.data)

            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_edit_response(serializer.data)