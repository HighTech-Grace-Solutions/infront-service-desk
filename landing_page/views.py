from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from iam.decorators import unauthenticated_user, allowed_users, admin_only

@login_required(login_url='login')
@allowed_users(allowed_role=['Customer'])
def landingPage(request):
    return render(request, 'landing_page.html')