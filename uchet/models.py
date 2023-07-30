from django.db import models
from datetime import datetime

class journal(models.Model):
    number = models.SmallIntegerField(default=None)
    date_purch = models.DateField()
    acc = models.SmallIntegerField()
    work_hours = models.CharField(max_length=30)
    malf = models.CharField(max_length=30)
    date_rep = models.DateField(null=True)

class journ_bat(models.Model):
    date = models.DateField()
    work_hours = models.TimeField()
    number = models.SmallIntegerField()

class car(models.Model):
    date_purch = models.DateField()
    acc = models.SmallIntegerField()
    work_hours = models.TimeField()
    number = models.SmallIntegerField()
    guarant = models.SmallIntegerField()

class battery(models.Model):
    number = models.SmallIntegerField()
    work_hours = models.TimeField()
    date_purch = models.DateField()
    guarant = models.SmallIntegerField()

    # Create your models here.
