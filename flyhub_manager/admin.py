from django.contrib import admin
from .models import (
    Airport,
    AirplaneType,
    Crew,
    Airplane,
)


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("name", "closest_big_city")
    search_fields = ("name", "closest_big_city")


@admin.register(AirplaneType)
class AirplaneTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "full_name")
    search_fields = ("first_name", "last_name")


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row", "airplane_type", "seats_count")
    search_fields = ("name", "airplane_type__name")
    list_filter = ("airplane_type",)
