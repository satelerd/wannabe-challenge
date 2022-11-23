from django.db import models


# For this challenge, we expect you to develop an API on Node.js that allows you to create, update, delete and get the data about airports, airlines, and flights attached to this email.


# Create your models here.
class Airport(models.Model):
    iata_code = models.CharField(max_length=3)  
    airline = models.CharField(max_length=100)

