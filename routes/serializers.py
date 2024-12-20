from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from routes.models import Route


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ("distance", "source", "destination",)
