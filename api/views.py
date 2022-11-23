from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from api.models import Airport
from api.serializers import AirportSerializer


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