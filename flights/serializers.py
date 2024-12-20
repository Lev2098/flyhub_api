from rest_framework import serializers

from flights.models import Flight
from flyhub_manager.models import Crew


class FlightSerializer(serializers.ModelSerializer):
    crew = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Crew.objects.all()
    )

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
