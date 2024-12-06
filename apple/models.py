from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # phone = models.CharField(max_length=20)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=6)
    people = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    tablenumber = models.CharField(max_length=10)


class CustomUser():
    name = models.CharField(max_length=100)    
    password = models.CharField(max_length=100)