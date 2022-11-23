from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from api.models import Airport
from api.serializers import AirportSerializer

from api.models import Airline
from api.serializers import AirlineSerializer

from api.models import Flight
from api.serializers import FlightSerializer


# For this challenge, we expect you to develop an API on Node.js that allows you to create, update, delete and get the data about airports, airlines, and flights attached to this email.

class AirportListView(APIView):
    """
    List all airports, or create a new airport.
    """
    def get(self, request, format=None):
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        airports = Airport.objects.all()
        airports.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, format=None):
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirlineListView(APIView):
    """
    List all airlines, or create a new airline.
    """
    def get(self, request, format=None):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        airlines = Airline.objects.all()
        airlines.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, format=None):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightListView(APIView):
    """
    List all flights, or create a new flight.
    """
    def get(self, request, format=None):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        flights = Flight.objects.all()
        flights.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, format=None):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)