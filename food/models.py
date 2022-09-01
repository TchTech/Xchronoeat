from unicodedata import category
from django.db import models

class comfood(models.Model):
    index = models.IntegerField()
    name = models.TextField()
    gramms = models.IntegerField()
    proteins = models.FloatField()
    fats = models.FloatField()
    carbohydrates = models.FloatField()
    calories = models.FloatField()
    category = models.TextField()
