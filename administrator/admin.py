from django.contrib import admin
from .models import *
from account.models import *


# Register your models here.

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'email', 'group', 'last_ticket', 'round_robin_selected')
    # list_filter = ('email__company_link', 'group')

    def get_name(self, obj):
        return obj.email.full_name


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'round_robin')
    # list_filter = ('company_link', 'name')

    # def company(self, obj):
    #     return obj.company_link.name


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'PIC', 'email', 'round_robin')

