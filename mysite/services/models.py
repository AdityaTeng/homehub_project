from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

request_options = (
    ('PL', 'Plumbing'),
    ('EL', 'Electrical'),
    ('PA', 'Painting'),
    ('DC', 'Deep Cleaning'),
)


class Request(models.Model):
    request_type = models.CharField(max_length=100, choices=request_options)
    request_description = models.TextField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)
    alt_phone = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)