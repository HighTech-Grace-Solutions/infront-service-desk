from django.urls import path
from iam import views
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout', views.logoutUser, name='logout'),
    # path('home', views.home,name='home'),
    path('password', views.password, name='password'),
    path('error', views.unavailable_page, name='unavailable_page'),
]
