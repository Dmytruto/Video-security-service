from django.db import models

class Names(models.Model):
    name = models.CharField(max_length=100, default="")

class MovementHistory(models.Model):
    personNames = models.ManyToManyField(Names, blank = True)
    time_period = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
