from django.contrib import admin

from orders.models import Ticket, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("row", "seat", "flight", "order")
    list_filter = ("flight", "order")
    search_fields = ("order__user__username", "flight__route__source__name", "flight__route__destination__name")
