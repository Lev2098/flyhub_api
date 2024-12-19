from rest_framework import serializers

from flights.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    crew = serializers.StringRelatedField(many=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "route",
            "airplane",
            "crew",
            "departure_time",
            "arrival_time"
        )