from django.db import models

class DataPoint(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    is_categorical = models.BooleanField(default=False)