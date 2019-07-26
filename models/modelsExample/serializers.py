from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Food



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

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