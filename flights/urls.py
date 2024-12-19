from django.urls import path, include

from rest_framework import routers

from flights.views import FlightViewSet


app_name = "flight"


router = routers.DefaultRouter()

router.register("flight", FlightViewSet, basename="flight")

urlpatterns = [
    path("", include(router.urls))
]