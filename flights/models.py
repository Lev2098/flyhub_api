from django.db import models

from flyhub_manager.models import Airplane, Crew
from routes.models import Route


class Flight(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    crew = models.ManyToManyField(Crew)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return (f"ID({self.id}) | "
                f"TIME {self.departure_time} - {self.arrival_time}")
