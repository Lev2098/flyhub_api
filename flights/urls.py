from django.urls import path, include

from rest_framework import routers

from flights.views import FlightViewSet


app_name = "flights"


router = routers.DefaultRouter()

router.register("flight", FlightViewSet, basename="flight")

urlpatterns = [
    path("", include(router.urls))
]
