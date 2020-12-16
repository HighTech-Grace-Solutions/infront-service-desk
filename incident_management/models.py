from django.db import models
from django.db.models import Max
from datetime import datetime
from django.utils import timezone
from django_comments_xtd.models import XtdComment
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    #! FK to Category model
    parent_category = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Impact(models.Model):
    impact = models.IntegerField(default=-1)


class Urgency(models.Model):
    urgency = models.IntegerField(default=-1)

class Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default="")

    def __str__(self):
        return self.name

class IncidentTicket(models.Model):
    ticket_id = models.CharField(
        primary_key=True, unique=True, editable=False, max_length=10, default=None)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    title = models.CharField(max_length=500)
    ticket_type = models.ForeignKey('Type', on_delete=models.CASCADE, default="")
    description = models.TextField(max_length=500, null=True, blank=True, default="")
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    support_group = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    impact = models.IntegerField(default=-1)
    urgency = models.IntegerField(default=-1)
    priority = models.IntegerField(default=-1)
    company = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=20, default="")
    sla_response = models.DateTimeField(default=timezone.now)
    sla_resolution = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('incident_report', args=[str(self.ticket_id)])

    def save(self, **kwargs):
        if not self.ticket_id:
            # max = IncidentTicket.objects.aggregate(id_max=Max('ticket_id'))['id_max']
            # self.ticket_id  = "{}{:05d}".format("ID", max if max is not None else 1)
            custom = IncidentTicket.objects.count()
            # max = custom.ticket_id

            if custom != None:
                temp = custom
                temp += 1
                custom = "{:05d}".format(temp)
            else:
                custom = '1'

            self.ticket_id = "{:05d}".format(int(custom[:]))
        super().save(*kwargs)

    def __str__(self):
        return self.ticket_id


class ReportComment(XtdComment):
    def save(self, *args, **kwargs):
        super(ReportComment, self).save(*args, **kwargs)
