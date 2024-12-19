from django.db import models

from flyhub_manager.models import Airport


class Route(models.Model):
    source = models.ForeignKey(Airport, related_name="departures", on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, related_name="arrivals", on_delete=models.CASCADE)
    distance = models.IntegerField()

    def __str__(self):
        return f"distance: {self.distance} km"