from concurrent.futures.process import _ThreadWakeup
from pyexpat import model
from statistics import mode
from django.db import models

class User(models.Model):
    email = models.CharField(blank=True, max_length=250)
    firstName = models.CharField(blank=True, max_length=200)
    password = models.CharField(blank=True, max_length=200)
    Confirm_password = models.CharField(blank=True, max_length=200)

