# elevators/models.py
from django.db import models


class Elevator(models.Model):
    operational = models.BooleanField(default=True)

class Floor(models.Model):
    number = models.PositiveIntegerField(unique=True)

class UserRequest(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    direction = models.CharField(choices=[('UP', 'Up'), ('DOWN', 'Down')], max_length=4)
