from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *

class AccountAdmin(UserAdmin):
    exclude = ('username',)
    # to display on the column
    list_display = ('email','role', 'group','is_staff', 'is_admin')
    #search specifier
    list_display = ('full_name', 'email', 'role', 'group', 'company_link')

    readonly_fields = ('date_joined','last_login')
    ordering = ('email','role', 'group',  'is_staff', 'is_admin')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)