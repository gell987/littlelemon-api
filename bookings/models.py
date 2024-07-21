# bookings/models.py

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
