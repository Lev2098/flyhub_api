from django.db import models
from rest_framework.exceptions import ValidationError

from flights.models import Flight
from flyhub_service import settings


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"created order at: {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="tickets", on_delete=models.CASCADE)

    @staticmethod
    def validate_ticket(row, seat, flight, error_to_raise):

        airplane = flight.airplane

        if not isinstance(row, int) or not isinstance(seat, int):
            raise error_to_raise({"row_seat": "Row and seat must be integers."})

        for ticket_attr_value, ticket_attr_name, airplane_attr_name in [
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(airplane, airplane_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name} "
                                          f"number must be in the available range: "
                                          f"(1, {airplane_attr_name}): "
                                          f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        if not self.flight:
            raise ValidationError({"flight": "Flight must be provided."})
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.flight,
            ValidationError,
        )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Ticket, self).save(*args, **kwargs)

    def __str__(self):

        user_info = self.order.user.id \
            if self.order and self.order.user \
            else "Unknown User"

        return (
            f"Ordered by:{user_info} "
            f"Row: {self.row}, "
            f"Seat: {self.seat}, "
            f"Flight: {self.flight}"
                )
