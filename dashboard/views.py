from django.shortcuts import render
from django.views import generic
from iam.decorators import unauthenticated_user, allowed_users, admin_only

@allowed_users(allowed_role=['Admin', 'Technician'])
def dashboard(request):
    return render(request, 'dashboard.html')
