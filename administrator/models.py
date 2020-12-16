from django.db import models
from django.conf import settings
from account.models import Account
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    company_id = models.IntegerField(default=1, unique=True)
    name = models.CharField(max_length=50, unique=True)
    PIC = models.CharField(max_length=255, blank=True, null=True, default="Not Set")
    email = models.CharField(max_length=100, unique=True)
    domain = models.CharField(max_length=50, unique=True, blank=True, null=True)
    contact_number = models.CharField(max_length=12, blank=True, null=True, default="")
    round_robin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    round_robin = models.BooleanField(default=False)
    # company_link = models.ForeignKey("Company", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Technician(models.Model):
    email = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    last_ticket = models.DateTimeField(default=timezone.now)
    round_robin_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.email.full_name