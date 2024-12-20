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
        fields = "__all__"


class AirplaneSerializer(serializers.ModelSerializer):
    airplane_type_name = AirplaneTypeSerializer(
        source="airplane_type", read_only=False)

    class Meta:
        model = Airplane
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "seats_count",
            "airplane_type_name",
        )

    def create(self, validated_data):
        airplane_type_data = validated_data.pop("airplane_type")
        airplane_type = AirplaneType.objects.create(**airplane_type_data)
        airplane = Airplane.objects.create(
            airplane_type=airplane_type, **validated_data
        )
        return airplane


class AirplaneDetailSerializer(serializers.ModelSerializer):
    airplane_type = AirplaneTypeSerializer()

    class Meta:
        model = Airplane
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "seats_count",
            "airplane_type",
            "airplane_type_name",
        )


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = "__all__"
