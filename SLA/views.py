from django.shortcuts import render, get_object_or_404, redirect
from iam.decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponse
from incident_management.models import *
from .models import *
from administrator.models import *
from datetime import datetime, date, time, timedelta
from calendar import HTMLCalendar
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse


@allowed_users(allowed_role=['Admin'])
def SLA(request):
    user_account = Technician.objects.all()
    Company_Var = Company.objects.all()
    Calendars = SLATable.objects.all()
    return render(request, 'SLA.html', {
        'user': user_account,
        'cn': Company_Var,
        'calendar': Calendars,
    })


@allowed_users(allowed_role=['Admin'])
def save_sla_form(request):

    new_company = SLATable(

        priority1=1,
        FRT1=request.POST['FirstResponseTime1'],
        ERT1=request.POST['EveryResponseTime1'],
        RT1=request.POST['ResolutionTime1'],
        priority2=2,
        FRT2=request.POST['FirstResponseTime2'],
        ERT2=request.POST['EveryResponseTime2'],
        RT2=request.POST['ResolutionTime2'],
        priority3=3,
        FRT3=request.POST['FirstResponseTime3'],
        ERT3=request.POST['EveryResponseTime3'],
        RT3=request.POST['ResolutionTime3'],
        priority4=4,
        FRT4=request.POST['FirstResponseTime4'],
        ERT4=request.POST['EveryResponseTime4'],
        RT4=request.POST['ResolutionTime4'],


    )

    new_company.save()
    return redirect('SLA')


@allowed_users(allowed_role=['Admin'])
def company_slainfo(request):
    Company_Var = Company.objects.all()
    Company_Val = int(request.POST['company_name'])
    request.session['company_name_views'] = Company_Val

    if (Company_Val == 1):
        SLATable_objs = SLATable.objects.get(CompanyUserName=1)
        return render(request, 'SLA.html',
                      {'sla_display': SLATable_objs,
                       'cn': Company_Var,
                       'cval': Company_Val})

    elif (Company_Val == 2):
        SLATable_objs = SLATable.objects.get(CompanyUserName=2)
        return render(request, 'SLA.html',
                      {'sla_display': SLATable_objs,
                       'cn': Company_Var,
                       'cval': Company_Val})

    else:
        SLATable_objs = SLATable.objects.get(CompanyUserName=3)
        return render(request, 'SLA.html',
                      {'sla_display': SLATable_objs,
                       'cn': Company_Var,
                       'cval': Company_Val})


@allowed_users(allowed_role=['Admin'])
def sla_update(request):

    Company_Val = int(request.POST['company_name'])
    sla_set = SLATable.objects.get(CompanyUserName=Company_Val)
    sla_set.FRT1 = request.POST['FirstResponseTime1']
    sla_set.ERT1 = request.POST['EveryResponseTime1']
    sla_set.RT1 = request.POST['ResolutionTime1']
    sla_set.FRT2 = request.POST['FirstResponseTime2']
    sla_set.ERT2 = request.POST['EveryResponseTime2']
    sla_set.RT2 = request.POST['ResolutionTime2']
    sla_set.FRT3 = request.POST['FirstResponseTime3']
    sla_set.ERT3 = request.POST['EveryResponseTime3']
    sla_set.RT3 = request.POST['ResolutionTime3']
    sla_set.FRT4 = request.POST['FirstResponseTime4']
    sla_set.ERT4 = request.POST['EveryResponseTime4']
    sla_set.RT4 = request.POST['ResolutionTime4']
    sla_set.save()

    return redirect('SLA')


@allowed_users(allowed_role=['Admin'])
def sla_calculation(request):
    # SLATable_objs = SLATable.objects.all()
    # IncidentTicket_objs = IncidentTicket.objects.get(
    #     ticket_id='ID00003')  # Need to get latest created Tickets

    # Company_Val = int(request.POST['company_name'])

    # if (Company_Val == 1):
    #     SLATable_objs = SLATable.objects.get(CompanyUserName=1)
    #     if (priority == priority1):
    #         RT = SLATable_objs.RT1
    #         FRT = SLATable_objs.FRT1
    #         ERT = SLATable_objs.ERT1
    #         Hours = SLATable_objs.hours1

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     elif (priority == priority2):
    #         RT = SLATable_objs.RT2
    #         FRT = SLATable_objs.FRT2
    #         ERT = SLATable_objs.ERT2
    #         Hours = SLATable_objs.hours2

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     elif (priority == priority3):
    #         RT = SLATable_objs.RT3
    #         FRT = SLATable_objs.FRT3
    #         ERT = SLATable_objs.ERT3
    #         Hours = SLATable_objs.hours3

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     else:
    #         RT = SLATable_objs.RT4
    #         FRT = SLATable_objs.FRT4
    #         ERT = SLATable_objs.ERT4
    #         Hours = SLATable_objs.hours4

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    # elif (Company_Val == 2):
    #     SLATable_objs = SLATable.objects.get(CompanyUserName=2)
    #     if (priority == priority1):
    #         RT = SLATable_objs.RT1
    #         FRT = SLATable_objs.FRT1
    #         ERT = SLATable_objs.ERT1
    #         Hours = SLATable_objs.hours1

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     elif (priority == priority2):
    #         RT = SLATable_objs.RT2
    #         FRT = SLATable_objs.FRT2
    #         ERT = SLATable_objs.ERT2
    #         Hours = SLATable_objs.hours2

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     elif (priority == priority3):
    #         RT = SLATable_objs.RT3
    #         FRT = SLATable_objs.FRT3
    #         ERT = SLATable_objs.ERT3
    #         Hours = SLATable_objs.hours3

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     else:
    #         RT = SLATable_objs.RT4
    #         FRT = SLATable_objs.FRT4
    #         ERT = SLATable_objs.ERT4
    #         Hours = SLATable_objs.hours4

    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    # else:
    #     SLATable_objs = SLATable.objects.get(CompanyUserName=3)
    #     if (priority == priority1):
    #         RT = SLATable_objs.RT1
    #         FRT = SLATable_objs.FRT1
    #         ERT = SLATable_objs.ERT1
    #         Hours = SLATable_objs.hours1
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     elif (priority == priority2):
    #         RT = SLATable_objs.RT2
    #         FRT = SLATable_objs.FRT2
    #         ERT = SLATable_objs.ERT2
    #         Hours = SLATable_objs.hours2
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     elif (priority == priority3):
    #         RT = SLATable_objs.RT3
    #         FRT = SLATable_objs.FRT3
    #         ERT = SLATable_objs.ERT3
    #         Hours = SLATable_objs.hours3
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()
    #     else:
    #         RT = SLATable_objs.RT4
    #         FRT = SLATable_objs.FRT4
    #         ERT = SLATable_objs.ERT4
    #         Hours = SLATable_objs.hours4
    #         ST = SLATable_objs.MonST
    #         ET = SLATable_objs.MonET

    #         CD = IncidentTicket_objs.date_created

    #         ST_hour = int(ST.strftime("%H"))
    #         ET_hour = int(ET.strftime("%H"))

    #         Workhours = ET_hour - ST_hour
    #         if date().today().isoweekday() == 5:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 72
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 6:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 48
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         elif date().today().isoweekday() == 7:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #         else:
    #             if (RT < Workhours):
    #                 Deadline = (CD + timedelta(hours=RT)).time()
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    #             else:
    #                 Diff = RT - Workhours + 24
    #                 Deadline = CD + timedelta(hours=Diff)
    #                 SLATable_objs.Deadline = Deadline
    #                 IncidentTicket_objs.sla_resolution = Deadline
    #                 SLATable_objs.save()
    #                 IncidentTicket_objs.save()

    return HttpResponse("Yup")


@allowed_users(allowed_role=['Admin'])
def PMatrix(request):
    return render(request, 'PMatrix.html')


@allowed_users(allowed_role=['Admin'])
def Calendar(request):
    print("lol")
    return render(request, 'Calendar.html')


def MatrixUpdate(request):
    # Company_Val = int(request.POST['priority_company_name']),
    Company_Val = request.session['company_name_views']
    print(Company_Val)
    # print(request.session.get('meow'))
    UN1 = request.POST['UrgencyName1']
    UN2 = request.POST['UrgencyName2']
    UN3 = request.POST['UrgencyName3']
    IN1 = request.POST['ImpactName1']
    IN2 = request.POST['ImpactName2']
    IN3 = request.POST['ImpactName3']
    UNum1 = int(request.POST['UrgencyNumber1'])
    UNum2 = int(request.POST['UrgencyNumber2'])
    UNum3 = int(request.POST['UrgencyNumber3'])
    Inum1 = int(request.POST['ImpactNumber1'])
    Inum2 = int(request.POST['ImpactNumber2'])
    Inum3 = int(request.POST['ImpactNumber3'])
    matrix_set = SLATable.objects.get(CompanyUserName=Company_Val)
    matrix_set.UrgencyName1 = UN1
    matrix_set.UrgencyName2 = UN2
    matrix_set.UrgencyName3 = UN3
    matrix_set.ImpactName1 = IN1
    matrix_set.ImpactName2 = IN2
    matrix_set.ImpactName3 = IN3
    matrix_set.UrgencyNumber1 = UNum1
    matrix_set.UrgencyNumber2 = UNum2
    matrix_set.UrgencyNumber3 = UNum3
    matrix_set.ImpactNumber1 = Inum1
    matrix_set.ImpactNumber2 = Inum2
    matrix_set.ImpactNumber3 = Inum3
    matrix_set.save()

    return redirect('SLA')


# input and pass holiday to template
def Calendar_Update(request):
    print("mEh")
    Company_Val = int(request.POST['priority_company_name'])
    Calendar_set = SLATable.objects.get(CompanyUserName=Company_Val)
    Calendar_set.Title = request.POST['Calendar_Title']
    Calendar_set.Timezone = request.POST['timezone_select']
    Calendar_set.Day = request.POST['day']
    Calendar_set.MonST = request.POST['ST1']
    Calendar_set.TueST = request.POST['ST2']
    Calendar_set.WedST = request.POST['ST3']
    Calendar_set.ThurST = request.POST['ST4']
    Calendar_set.FriST = request.POST['ST5']
    Calendar_set.MonET = request.POST['ET1']
    Calendar_set.TueET = request.POST['ET2']
    Calendar_set.WedET = request.POST['ET3']
    Calendar_set.ThurET = request.POST['ET4']
    Calendar_set.FriET = request.POST['ET5']

    Calendar_set.save()
    return render(request, 'SLA.html')


def Holiday_Update(request):
    print("Eh")
    D = request.POST['date']
    New_holiday = SLATable(
        Date=D,
        Holiday=request.POST['holiday']
    )

    New_holiday.save()
    return render(request, 'SLA.html')
