from django.db import models


# For this challenge, we expect you to develop an API on Node.js that allows you to create, update, delete and get the data about airports, airlines, and flights attached to this email.


# Create your models here.
class Airport(models.Model):
    iata_code = models.CharField(max_length=3)  
    airport = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    country = models.CharField(max_length=100, default="")
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


class Airline(models.Model):
    iata_code = models.CharField(max_length=3)
    airline = models.CharField(max_length=100)



# class Flight(models.Model):
#     # YEAR,MONTH,DAY,DAY_OF_WEEK,AIRLINE,FLIGHT_NUMBER,TAIL_NUMBER,ORIGIN_AIRPORT,DESTINATION_AIRPORT,SCHEDULED_DEPARTURE,DEPARTURE_TIME,DEPARTURE_DELAY,TAXI_OUT,WHEELS_OFF,SCHEDULED_TIME,ELAPSED_TIME,AIR_TIME,DISTANCE,WHEELS_ON,TAXI_IN,SCHEDULED_ARRIVAL,ARRIVAL_TIME,ARRIVAL_DELAY,DIVERTED,CANCELLED,CANCELLATION_REASON,AIR_SYSTEM_DELAY,SECURITY_DELAY,AIRLINE_DELAY,LATE_AIRCRAFT_DELAY,WEATHER_DELAY
#     year = models.IntegerField()
#     month = models.IntegerField()
#     day = models.IntegerField()
#     day_of_week = models.IntegerField()
#     airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
#     flight_number = models.IntegerField()
#     tail_number = models.CharField(max_length=100)
#     origin_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origin_airport")
#     destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination_airport")
#     scheduled_departure = models.IntegerField()
#     departure_time = models.IntegerField()
#     departure_delay = models.IntegerField()
#     taxi_out = models.IntegerField()
#     wheels_off = models.IntegerField()
#     scheduled_time = models.IntegerField()
#     elapsed_time = models.IntegerField()
#     air_time = models.IntegerField()
#     distance = models.IntegerField()
#     wheels_on = models.IntegerField()
#     taxi_in = models.IntegerField()
#     scheduled_arrival = models.IntegerField()
#     arrival_time = models.IntegerField()
#     arrival_delay = models.IntegerField()
#     diverted = models.IntegerField()
#     cancelled = models.IntegerField()
#     cancellation_reason = models.CharField(max_length=100)
#     air_system_delay = models.IntegerField()
#     security_delay = models.IntegerField()
#     airline_delay = models.IntegerField()
#     late_aircraft_delay = models.IntegerField()
#     weather_delay = models.IntegerField()

