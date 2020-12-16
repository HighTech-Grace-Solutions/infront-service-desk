from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SLATable)
admin.site.register(PriorityMatrix)
admin.site.register(HolidayDB)


# @admin.register(Priority)
# class PriorityAdmin(admin.ModelAdmin):
#     list_display = ('priority_val', 'priority_name', 'company_link')
#     list_filter = ('company_link', 'priority_val')


# @admin.register(Impact)
# class ImpactAdmin(admin.ModelAdmin):
#     list_display = ('impact_val', 'impact_name',
#                     'priority_link', 'company_link')
#     list_filter = ('company_link', 'priority_link')


# @admin.register(Urgency)
# class UrgencyAdmin(admin.ModelAdmin):
#     list_display = ('urgency_val', 'urgency_name',
#                     'priority_link', 'company_link')
#     list_filter = ('company_link', 'priority_link')
