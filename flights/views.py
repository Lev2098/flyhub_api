from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from flights.models import Flight
from flights.serializers import FlightSerializer


class FlightViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer