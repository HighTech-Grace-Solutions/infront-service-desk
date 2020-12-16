from django.db import models
import datetime
from administrator.models import *


class SLATable(models.Model):

	CompanyUserName = models.IntegerField(default=1)
	priority1 = models.IntegerField(default=1)
	priority2 = models.IntegerField(default=1)
	priority3 = models.IntegerField(default=1)
	priority4 = models.IntegerField(default=1)
	FRT1 = models.IntegerField(default=15)
	ERT1 = models.IntegerField(default=1)
	RT1 = models.IntegerField(default=1)
	FRT2 = models.IntegerField(default=15)
	ERT2 = models.IntegerField(default=1)
	RT2 = models.IntegerField(default=1)
	FRT3 = models.IntegerField(default=15)
	ERT3 = models.IntegerField(default=1)
	RT3 = models.IntegerField(default=1)
	FRT4 = models.IntegerField(default=15)
	ERT4 = models.IntegerField(default=1)
	RT4 = models.IntegerField(default=1)
	Title = models.CharField(max_length=255)
	Timezone = models.CharField(max_length=255, null=True, blank=True)
	MonST = models.TimeField(null=True, blank=True)
	TueST = models.TimeField(null=True, blank=True)
	WedST = models.TimeField(null=True, blank=True)
	ThurST = models.TimeField(null=True, blank=True)
	FriST = models.TimeField(null=True, blank=True)
	MonET = models.TimeField(null=True, blank=True)
	TueET = models.TimeField(null=True, blank=True)
	WedET = models.TimeField(null=True, blank=True)
	ThurET = models.TimeField(null=True, blank=True)
	FriET = models.TimeField(null=True, blank=True)
	Deadline = models.DateTimeField(null=True, blank=True)


class PriorityMatrix(models.Model):

	UrgencyName1 = models.CharField(max_length=50)
	UrgencyName2 = models.CharField(max_length=50)
	UrgencyName3 = models.CharField(max_length=50)
	ImpactName1 = models.CharField(max_length=50)
	ImpactName2 = models.CharField(max_length=50)
	ImpactName3 = models.CharField(max_length=50)
	UrgencyNumber1 = models.IntegerField(null=True, blank=True)
	UrgencyNumber2 = models.IntegerField(null=True, blank=True)
	UrgencyNumber3 = models.IntegerField(null=True, blank=True)
	ImpactNumber1 = models.IntegerField(null=True, blank=True)
	ImpactNumber2 = models.IntegerField(null=True, blank=True)
	ImpactNumber3 = models.IntegerField(null=True, blank=True)


class HolidayDB(models.Model):
	Date = models.CharField(max_length=255, null=True, blank=True)
	Holiday = models.CharField(max_length=255, null=True, blank=True)


# class Priority(models.Model):
# 	priority_val = models.IntegerField(null=True, blank=True)
# 	priority_name = models.CharField(max_length=50, null=True, blank=True)
# 	FRT = models.IntegerField(null=True, blank=True)
# 	ERT = models.IntegerField(null=True, blank=True)
# 	RT = models.IntegerField(null=True, blank=True)
# 	company_link = models.ForeignKey(
# 		'administrator.Company', on_delete=models.CASCADE, default="")

# 	# def __str__(self):
# 	# 	return self.company_link.name + " - " + str(self.priority_val) + " (" + self.priority_name + ")"

# 	def __str__(self):
# 		return self.priority_name
		
# class Impact(models.Model):
# 	impact_val = models.IntegerField(default=-1)
# 	impact_name = models.CharField(max_length=50, null=True, blank=True)
# 	priority_link = models.ForeignKey(
# 		'Priority', on_delete=models.CASCADE, default="")
# 	company_link = models.ForeignKey(
# 		'administrator.Company', on_delete=models.CASCADE, default="")


# class Urgency(models.Model):
# 	urgency_val = models.IntegerField(default=-1)
# 	urgency_name = models.CharField(max_length=50, null=True, blank=True)
# 	priority_link = models.ForeignKey(
# 		'Priority', on_delete=models.CASCADE, default="")
# 	company_link = models.ForeignKey(
# 		'administrator.Company', on_delete=models.CASCADE, default="")
