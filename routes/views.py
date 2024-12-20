from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from routes.models import Route
from routes.serializers import RouteSerializer


class RouteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Route.objects.all().select_related("source", "destination")
    serializer_class = RouteSerializer
