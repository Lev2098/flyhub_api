from django.urls import include, path

from rest_framework import routers

from routes.views import RouteViewSet

app_name = "routes"

router = routers.DefaultRouter()

router.register("route", RouteViewSet, basename="route")

urlpatterns = [
    path("", include(router.urls)),
]
