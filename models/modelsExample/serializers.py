from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = (
            'pk',
            'name',
            'description',
            'price',
            'quanity'
        )


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = (
            'pk',
            'name',
            'description',
            'price',
            'quanity'
        )
