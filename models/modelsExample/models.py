from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, int_list_validator

# Create your models here.
class Food(models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=100, blank=False)
    price = models.FloatField(max_length=10, blank=False)
    quanity = models.IntegerField(
        blank=False, default=0,  validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name