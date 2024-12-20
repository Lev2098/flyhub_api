from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from orders.models import Order, Ticket


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
        )


class TicketSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs=attrs)
        Ticket.validate_ticket(
            attrs["row"], attrs["seat"], attrs["flight"], ValidationError
        )
        return data

    def create(self, validated_data):
        if Ticket.objects.filter(
            row=validated_data["row"],
            seat=validated_data["seat"],
            flight=validated_data["flight"],
        ).exists():
            raise serializers.ValidationError(
                f"Seat {validated_data['row']}-"
                f"{validated_data['seat']} for flight "
                f"{validated_data['flight']} is already taken."
            )
        return super().create(validated_data)

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "flight", "order")
