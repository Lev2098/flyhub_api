from django.contrib import admin

from flights.forms import FlightForm
from flights.models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    form = FlightForm
    list_display = ("route", "airplane", "departure_time", "arrival_time")
    list_filter = ("route", "airplane", "departure_time")
    search_fields = ("route__source__name", "route__destination__name")
