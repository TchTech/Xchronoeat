from unicodedata import category
from django.db import models

class CommonFood(models.Model):
    index = models.IntegerField(unique=True)
    name = models.TextField(max_length=100)
    gramms = models.IntegerField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    calories = models.FloatField()
    category = models.TextField()
