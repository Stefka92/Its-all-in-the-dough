from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings


class Table(models.Model):
    code = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    image = CloudinaryField('table_image')

    def __str__(self):
        return self.code


class Booking(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
    )

    class Meta:
        ordering = ['date', 'start_time']


class BookingQuery(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

    # Add other fields specific to the Customer model