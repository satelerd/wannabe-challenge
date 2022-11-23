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



# For testing purposes (delete later)):
# a airport endpoint application/json body example:
# {
#     "iata_code": "JFK",
#     "airport": "John F Kennedy International Airport",
#     "city": "New York",
#     "state": "NY",
#     "country": "United States",
#     "latitude": 40.639751,
#     "longitude": -73.778925
# }

# a airline endpoint application/json body example:
# {
#     "iata_code": "AA",
#     "airline": "American Airlines Inc."
# }

# a flight endpoint application/json body example:
# {
#     "year": 2015,
#     "month": 1,
#     "day": 1,
#     "day_of_week": 4,
#     "airline": 1,
#     "flight_number": 98,
#     "tail_number": "N407AS",
#     "origin_airport": "ANC",
#     "destination_airport": "SEA",
#     "scheduled_departure": "05:15:00",
#     "departure_time": "05:14:00",
#     "departure_delay": -1,
#     "taxi_out": 21,
#     "wheels_off": "05:35:00",
#     "scheduled_time": 205,
#     "elapsed_time": 194,
#     "air_time": 169,
#     "distance": 1448,
#     "wheels_on": "07:09:00",
#     "taxi_in": 4,
#     "scheduled_arrival": "07:20:00",
#     "arrival_time": "07:13:00",
#     "arrival_delay": -7,
#     "diverted": false,
#     "cancelled": false,
#     "cancellation_reason": "N/A",
#     "air_system_delay": 0,
#     "security_delay": 0,
#     "airline_delay": 0,
#     "late_aircraft_delay": 0,
#     "weather_delay": 0
# }