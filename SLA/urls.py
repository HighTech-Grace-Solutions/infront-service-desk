"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.SLA, name='SLA'),
    path('save_sla_form', views.save_sla_form, name="save_sla_form"),
    path('company_slainfo', views.company_slainfo, name="company_slainfo"),
    path('sla_calculation', views.sla_calculation, name="sla_calculation"),
    path('Calendar', views.Calendar, name="Calendar"),
    path('sla_update', views.sla_update, name="sla_update"),
    path('Holiday_Update', views.Holiday_Update, name="Holiday_Update"),
    path('Calendar_Update', views.Calendar_Update, name="Calendar_Update"),
    path('PMatrix', views.PMatrix, name="PMatrix"),
    path('MatrixUpdate', views.MatrixUpdate, name="MatrixUpdate"),

]
