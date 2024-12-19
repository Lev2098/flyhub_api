from rest_framework import serializers

from flyhub_manager.models import (
    Airport,
    Airplane,
    Crew,
    AirplaneType,

)


class AirplaneTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = '__all__'


class AirplaneSerializer(serializers.ModelSerializer):

    airplane_type_name = serializers.CharField(source="airplane_type.name")

    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "seats_count", "airplane_type_name",)


class AirplaneDetailSerializer(AirplaneSerializer):

    airplane_type = AirplaneTypeSerializer

    class Meta:
        model = Airplane
        fields = ("id", "name", "rows", "seats_in_row", "seats_count", "airplane_type_id", "airplane_type_name",)


class CrewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crew
        fields = '__all__'
