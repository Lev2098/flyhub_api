from django.urls import path, include
from rest_framework import routers

from flyhub_manager.views import (
    AirportViewSet,
    AirplaneViewSet,
    AirPlaneTypeViewSet,
    CrewViewSet,
)


app_name = "flyhub_manager"

router = routers.DefaultRouter()

router.register("airports", AirportViewSet, basename="airports")
router.register("airplane", AirplaneViewSet, basename="airplane")
router.register(
    "airplanetype",
    AirPlaneTypeViewSet,
    basename="airplanetype"
)
router.register("crew", CrewViewSet, basename="crew")


urlpatterns = [
    path("", include(router.urls))
]
