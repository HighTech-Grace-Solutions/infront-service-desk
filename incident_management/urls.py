from django.urls import path
from . import views

urlpatterns = [
    # path("overview", views.incident_ticket_overview, name="incident_ticket_overview"),
    # path("report", views.incident_report, name="incident_report"),

    
    path("form_test", views.email_test, name="email_test"),
    path("success", views.successView, name="success"),

    path("form", views.incident_form, name="incident_form"),
    
    # path("form", views.IncidentForm.as_view(), name="incident_form"),

    path("form_process", views.form_process, name="form_process"),

    path("ticket_update", views.ticket_update, name="ticket_update"),

    # path("overview", views.IncidentTicketOverview.as_view(),
    #      name="incident_ticket_overview"),

    path("overview", views.incident_overview,
         name="incident_ticket_overview"),

    path("report/<str:pk>", views.incident_report, name="incident_report"),

    path("report/<str:pk>", views.ticket_update, name="ticket_update"),
    
    path("overview/<str:pk>", views.incident_preview, name="incident_preview"),
]
