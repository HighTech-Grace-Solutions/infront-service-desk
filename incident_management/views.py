import operator
import itertools
import numpy as np
from .models import *
from SLA.models import *
from django_comments_xtd.views import notify_comment_followers
from administrator.models import *
from .forms import *
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from datetime import datetime, date, time, timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from iam.decorators import unauthenticated_user, allowed_users, admin_only
from django_comments_xtd.models import XtdComment
from django.conf import settings

from ServiceDesk.settings import EMAIL_HOST_USER
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.template import loader

# def incident_ticket_overview(request):
#     return render(request, 'incident_overview.html', {})

# def incident_report(request):
#     return render(request, 'incident_report.html', {})

# def incident_form(request):
#     return render(request, 'incident_form.html', {})

# class IncidentForm(ListView):
#     model = Technician
#     template_name = 'incident_form.html'
#     context_object_name = 'technician'


def form_test(request):
	return render(request, 'form_test.html', {})

# --------------------------- INCIDENT FORM PROCESS -------------------------- #


@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def email_test(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']

			html_message_template = loader.get_template("email_template.html")
			text_message_template = loader.get_template("email_template.txt")

			message_context = {'name': request.user.full_name,
							   'message': message}

			text_message = text_message_template.render(message_context)
			html_message = html_message_template.render(message_context)

			try:
				send_mail(subject, text_message, from_email,
				  [EMAIL_HOST_USER], html_message=html_message)
				# send_mail(subject, message, sender, [recipient])

			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "form_test.html", {'form': form})


@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def successView(request):
	return HttpResponse('Success! Thank you for your message.')


@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def form_process(request):
	priority_temp = 0
	impact_val = int(request.POST['inputImpact'])
	urgency_val = int(request.POST['inputUrgency'])
	sla_resp_val = request.POST['inputSLA_Response']
	sla_reso_val = request.POST['inputSLA_Resolution']

	if (impact_val == 1 and urgency_val == 1):
		priority_temp = 1
	elif ((impact_val == 2 and urgency_val == 1) or
		  (impact_val == 1 and urgency_val == 2)):
		priority_temp = 2
	elif ((impact_val == 1 and urgency_val == 3) or
		  (impact_val == 2 and urgency_val == 2) or
		  (impact_val == 3 and urgency_val == 1)):
		priority_temp = 3
	elif ((impact_val == 3 and urgency_val == 2) or
		  (impact_val == 2 and urgency_val == 3) or
		  (impact_val == 3 and urgency_val == 3)):
		priority_temp = 4

	support_group_val = request.POST['inputSupportGroup']
	assigned_to_val = request.POST['inputAssignee']
	name_val = request.POST['name']
	email_val = request.POST['email']
	title_val = request.POST['title']
	ticket_type_val = request.POST['type']
	description_val = request.POST['description']
	category_val = request.POST['inputCategory']
	sub_category_val = request.POST['inputSubcategory']

	new_ticket = IncidentTicket(
		name=name_val,
		email=email_val,
		title=title_val,
		ticket_type=Type.objects.get(name=ticket_type_val),
		description=description_val,
		category=category_val,
		sub_category=sub_category_val,
		support_group=support_group_val,
		assigned_to=assigned_to_val,
		impact=impact_val,
		urgency=urgency_val,
		priority=priority_temp,
		state="Open",
		sla_response=sla_resp_val,
		sla_resolution=sla_reso_val,
	)

	# Change last_ticket datetime of corresponding technician
	technician_pair = Technician.objects.get(email__full_name=assigned_to_val)
	technician_pair.last_ticket = datetime.now()
	technician_pair.save()

	# Save ticket changes
	new_ticket.save()
	latest_ticket = IncidentTicket.objects.last()

	# Send email to user's email (Reported By)
	subject = "New Ticket Submitted ({})".format(latest_ticket.ticket_id)

	html_message_template = loader.get_template("ticket_submitted_email_template.html")
	text_message_template = loader.get_template("ticket_submitted_email_template.txt")

	message_context = {	'ticket': latest_ticket,
						'subject': subject}

	text_message = text_message_template.render(message_context)
	html_message = html_message_template.render(message_context)

	send_mail(subject, text_message, EMAIL_HOST_USER,
		[email_val], html_message=html_message)
	# send_mail(subject, message, sender, [recipient])

	# return HttpResponse("SUCCESS")
	# Redirect to its corresponding incident report page
	return redirect('incident_report', new_ticket.ticket_id)


# ------------------------------- TICKET UPDATE ------------------------------ #

@allowed_users(allowed_role=['Admin', 'Technician'])
def ticket_update(request):
	priority_temp = 0
	impact_val = int(request.POST['inputImpact'])
	urgency_val = int(request.POST['inputUrgency'])
	support_group_val = request.POST['inputSupportGroup']
	assigned_to_val = request.POST['inputAssignee']
	category_val = request.POST['inputCategory']
	sub_category_val = request.POST['inputSubcategory']

	if (impact_val == 1 and urgency_val == 1):
		priority_temp = 1
	elif ((impact_val == 2 and urgency_val == 1) or
		  (impact_val == 1 and urgency_val == 2)):
		priority_temp = 2
	elif ((impact_val == 1 and urgency_val == 3) or
		  (impact_val == 2 and urgency_val == 2) or
		  (impact_val == 3 and urgency_val == 1)):
		priority_temp = 3
	elif ((impact_val == 3 and urgency_val == 2) or
		  (impact_val == 2 and urgency_val == 3) or
		  (impact_val == 3 and urgency_val == 3)):
		priority_temp = 4

	# Save changes of ticket fields based on incident ID
	ticket_id = request.POST['ticket_id']
	ticket_set = IncidentTicket.objects.get(ticket_id=ticket_id)
	assigned_to_old = ticket_set.assigned_to
	ticket_set.support_group = support_group_val
	ticket_set.assigned_to = assigned_to_val
	ticket_set.category = category_val
	ticket_set.sub_category = sub_category_val
	ticket_set.impact = impact_val
	ticket_set.urgency = urgency_val
	ticket_set.priority = priority_temp
	ticket_set.save()

	# Change last_ticket datetime of corresponding technician
	if (assigned_to_old != assigned_to_val):
		technician_pair = Technician.objects.get(
			email__full_name=assigned_to_val)
		technician_pair.last_ticket = datetime.now()
		technician_pair.save()

	# Redirect back to the Report page after applying changes (refresh)
	return redirect('incident_report', ticket_id)

# ----------------------- INCIDENT TICKET OVERVIEW PAGE ---------------------- #

# class IncidentTicketOverview(ListView):
#     model = IncidentTicket
#     template_name = 'incident_overview.html'
#     context_object_name = 'incident_ticket'


@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def incident_overview(request):
	if request.user.is_authenticated and request.user.role == 'Customer':
		incident_ticket_user = IncidentTicket.objects.filter(
			email=request.user.email)
		return render(request, 'incident_overview.html',
					  {'incident_ticket': incident_ticket_user})

	elif request.user.is_authenticated and (request.user.role == 'Admin' or request.user.role == 'Technician'):
		incident_ticket = IncidentTicket.objects.all()
		return render(request, 'incident_overview.html',
					  {'incident_ticket': incident_ticket})

# --------------------------- INCIDENT REPORT PAGE --------------------------- #


@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def incident_report(request, pk):
	technician_objs = Technician.objects.all()
	support_group_objs = Group.objects.all()
	category_objs = Category.objects.all()
	sub_category_objs = SubCategory.objects.all()
	source_objs = Source.objects.all()
	impact_objs = Impact.objects.all()
	urgency_objs = Urgency.objects.all()
	sla_objs = SLATable.objects.get(CompanyUserName=1)

	notify_comment_followers.subject = ("TEST SUBJECT")
	ticket = get_object_or_404(IncidentTicket, pk=pk)
	return render(request, 'incident_report.html',
				  {'report': ticket,
				   'technician_obj': technician_objs,
				   'support_group': support_group_objs,
				   'category': category_objs,
				   'sub_category': sub_category_objs,
				   'source': source_objs,
				   'impact': impact_objs,
				   'urgency': urgency_objs,
				   'sla': sla_objs})


# ------------------------ INCIDENT PREVIEW OFF-CANVAS ----------------------- #

@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def incident_preview(request, pk):
	ticket = get_object_or_404(IncidentTicket, pk=pk)
	return render(request, 'incident_preview.html', {'preview': ticket})

# ---------------------------- INCIDENT FORM PAGE ---------------------------- #


@allowed_users(allowed_role=['Admin', 'Technician', 'Customer'])
def incident_form(request):

	# Extract all technicians from groups with RR enabled
	technician_objs_round_robin = Technician.objects.filter(
		group__round_robin=True)

	# Store all RR-enabled technicians as a list
	technician_round_robin_list = []
	for tech in technician_objs_round_robin:
		technician_round_robin_list.append(tech)

	# Group all the RR-enabled technicians based on their support group
	get_attr = operator.attrgetter('group.name')
	technician_round_robin_grouped_list = [list(g) for k, g in itertools.groupby(
		sorted(technician_objs_round_robin, key=get_attr), get_attr)]

	# Case #1: When all technicians in RR have same last ticket DT
	if (all(v.last_ticket == technician_objs_round_robin[0].last_ticket for v in technician_objs_round_robin)):
		# Choose first technician in unsorted list by default
		# Admin side to rearrange default RR order is KIV
		technician_round_robin_selected = [i[0]
										   for i in technician_round_robin_grouped_list]

	# Case #2: When all technicians have been previously assigned to (different last_ticket values)
	else:
		technician_round_robin_sorted_list = []

		# Store sorted list of technicians based on groups into a new list
		for i in range(len(technician_round_robin_grouped_list)):
			technician_round_robin_sorted_list += [sorted(
				technician_round_robin_grouped_list[i], key=lambda x: x.last_ticket)]

		# Select the first person from each group
		technician_round_robin_selected_list = [
			i[0] for i in technician_round_robin_sorted_list]

		# Update the RR_selected status of each selected technician
		for tech in technician_round_robin_selected_list:
			tech.round_robin_selected = True
			tech.save()

		# Get the list of all the other technicians who are not selected for RR
		technician_round_robin_unselected = Technician.objects.filter(
			round_robin_selected=True)

		technician_round_robin_unselected_list = []

		for tech in technician_round_robin_unselected:
			technician_round_robin_unselected_list.append(tech)

		# Get the difference between the list of RR_selected and RR_unselected
		technician_round_robin_difference_list = (list(list(set(technician_round_robin_selected_list)-set(
			technician_round_robin_unselected_list)) + list(set(technician_round_robin_unselected_list)-set(technician_round_robin_selected_list))))

		for tech in technician_round_robin_difference_list:
			tech.round_robin_selected = False
			tech.save()

		# print(technician_round_robin_grouped_list)
		# print(technician_round_robin_sorted_list)
		# print(technician_round_robin_selected_list)
		# print(technician_round_robin_unselected_list)
		# print(technician_round_robin_difference_list)

	# Filter all technicians with Round Robin Selected status = False
	# (the rest of technicians who did not get selected for RR)
	technician_objs = Technician.objects.filter(round_robin_selected=False)
	support_group_objs = Group.objects.all()

	# Extract all data from necessary models
	category_objs = Category.objects.all()
	sub_category_objs = SubCategory.objects.all()
	source_objs = Source.objects.all()
	type_objs = Type.objects.all()

	#! IMPACT AND URGENCY MODELS ARE TEMPORARY (NEED TO TAKE FROM SLA)
	impact_objs = Impact.objects.all()
	urgency_objs = Urgency.objects.all()

	# Get current time
	current_time = timezone.now()

	#! TEMPORARY: Take SLA configuration of Company A
	sla_objs = SLATable.objects.get(CompanyUserName=1)

	ST = time(8, 30, 20, 804679)
	ET = time(17, 30, 20, 804679)
	RT = sla_objs.RT1
	CD = current_time

	ST_hour = int(ST.strftime("%H"))
	ET_hour = int(ET.strftime("%H"))

	Workhours = ET_hour - ST_hour

	# Ticket Resolution time is within working hours
	if ((CD + timedelta(hours=RT)).time() < ET and (CD + timedelta(hours=RT)).time() > ST):
		Deadline = (CD + timedelta(hours=RT))
		sla_objs.Deadline = Deadline

	else:
		# File ticket (outside working hours)
		if (CD.time() < ST or CD.time() > ET):
			ST_datetime = datetime.combine(datetime.now(), ST)
			Diff = (ST_datetime - CD)
			Deadline = CD + Diff + timedelta(hours=RT)
			sla_objs.Deadline = Deadline

		# Ticket filed within working hours but deadline overflows to next day
		else:
			Diff = RT - Workhours + 24
			Deadline = CD + timedelta(hours=Diff)
			sla_objs.Deadline = Deadline

	# return HttpResponse('Success!')
	return render(request, 'incident_form.html',
				  {
					  #   'form': form,
					  'technician_round_robin': technician_round_robin_selected_list,
					  'technician': technician_objs,
					  'support_group': support_group_objs,
					  'category': category_objs,
					  'type': type_objs,
					  'sub_category': sub_category_objs,
					  'source': source_objs,
					  'impact': impact_objs,
					  'urgency': urgency_objs,
					  'current_time': current_time,
					  'sla': sla_objs,
					  'deadline': Deadline})
