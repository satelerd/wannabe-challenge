from rest_framework import serializers

from api.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = (
            "iata_code",
            "airline",
        )