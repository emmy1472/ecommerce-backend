from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_vendor = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
