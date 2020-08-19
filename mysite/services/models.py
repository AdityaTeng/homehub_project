from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)

# Create your models here.

request_options = (
    ('PL', 'Plumbing'),
    ('EL', 'Electrical'),
    ('PA', 'Painting'),
    ('DC', 'Deep Cleaning'),
)

# class User(AbstractBaseUser, PermissionsMixin, models.Model):
#     username = models.CharField(max_length=100, unique=True)
#     # first_name = models.CharField(max_length=150, blank=True)
#     # last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(('date joined'), auto_now_add=True)

class Request(models.Model):
    request_type = models.CharField(max_length=100, choices=request_options)
    request_description = models.TextField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)
    alt_phone = models.IntegerField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
