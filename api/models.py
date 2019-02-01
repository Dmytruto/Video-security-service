from django.db import models
from django_mysql.models import ListCharField

# class Names(models.Model):
#     name = models.CharField(max_length=100)
#     names = models.ManyToManyField('self')

class MovementHistory(models.Model):
    personNames = ListCharField(
        base_field = models.CharField(max_length=50),
        size = 10,
        max_length = (510)
    )
    time_period = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
