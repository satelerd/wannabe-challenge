from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from api.models import Airport
from api.serializers import AirportSerializer

from api.models import Airline
from api.serializers import AirlineSerializer

from api.models import Flight
from api.serializers import FlightSerializer


class AirportListView(APIView):
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
    
    def patch(self, request, format=None,):
        airports = Airport.objects.all()
        airports = airports.get(id=request.data['id'])
        serializer = AirportSerializer(airports, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirlineListView(APIView):
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
    
    def patch(self, request, format=None):
        airlines = Airline.objects.all()
        airlines = airlines.get(id=request.data['id'])
        serializer = AirlineSerializer(airlines, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightListView(APIView):
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
    
    def patch(self, request, format=None):
        flights = Flight.objects.all()
        flights = flights.get(id=request.data['id'])
        serializer = FlightSerializer(flights, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)