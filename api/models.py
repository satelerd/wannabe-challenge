from django.db import models


# Create your models here.
class Airport(models.Model):
    iata_code = models.CharField(max_length=3, default="XXX")  
    airport = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


class Airline(models.Model):
    iata_code = models.CharField(max_length=3, default="XXX")
    airline = models.CharField(max_length=100, default="")


class Flight(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    day_of_week = models.IntegerField(default=0)
    airline = models.IntegerField(default=0)
    flight_number = models.IntegerField(default=0)
    tail_number = models.CharField(max_length=100, default="")
    origin_airport = models.CharField(max_length=100, default="")
    destination_airport = models.CharField(max_length=100, default="")
    scheduled_departure = models.TimeField(default="00:00:00")
    departure_time = models.TimeField(default="00:00:00")
    departure_delay = models.IntegerField(default=0)
    taxi_out = models.IntegerField(default=0)
    wheels_off = models.TimeField(default="00:00:00")
    scheduled_time = models.IntegerField(default=0)
    elapsed_time = models.IntegerField(default=0)
    air_time = models.IntegerField(default=0)
    distance = models.IntegerField(default=0)
    wheels_on = models.TimeField(default="00:00:00")
    taxi_in = models.IntegerField(default=0)
    scheduled_arrival = models.TimeField(default="00:00:00")
    arrival_time = models.TimeField(default="00:00:00")
    arrival_delay = models.IntegerField(default=0)
    diverted = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    cancellation_reason = models.CharField(max_length=100, default="")
    air_system_delay = models.IntegerField(default=0)
    security_delay = models.IntegerField(default=0)
    airline_delay = models.IntegerField(default=0)
    late_aircraft_delay = models.IntegerField(default=0)
    weather_delay = models.IntegerField(default=0)
