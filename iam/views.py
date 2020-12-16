from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import login, authenticate, logout
from account.models import Account
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def login(request):
    if request.method == ('POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username=email, password=password)

        if user is not None:

            auth.login(request, user)

            if request.user.role == 'Customer':
                return redirect('landing_page')

            else:
                return redirect('dashboard')

        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('login')

    else:
        return render(request, 'login.html',)


def logoutUser(request):
    auth.logout(request)
    return redirect('login')

def unavailable_page(request):
    return render(request, 'unavailable_page.html',)


def password(request):
    return render(request, 'password.html',)


def register(request):
    return render(request, 'register.html',)
