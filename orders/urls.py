from django.urls import include, path

from rest_framework import routers

from orders.views import OrderViewSet, TicketViewSet

app_name = "orders"

router = routers.DefaultRouter()

router.register("order", OrderViewSet, basename="order")
router.register("ticket", TicketViewSet, basename="ticket")

urlpatterns = [path("", include(router.urls))]
