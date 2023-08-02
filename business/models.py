from django.db import models
from django.utils import timezone
import datetime

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    mobile_number = models.BigIntegerField()
    email = models.EmailField(max_length=256)
    state = models.CharField(max_length=256)
    required_part = models.CharField(max_length=256)
    make = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    description = models.CharField(max_length=500)  # Increased max_length to 500
    image = models.FileField(upload_to="image/", max_length=256, null=True, default=None)
    time_difference_hours = 5.5
    default_datetime = timezone.now() + datetime.timedelta(hours=time_difference_hours)
    date_time = models.DateTimeField(default=default_datetime)

    def __str__(self):
        return self.name

