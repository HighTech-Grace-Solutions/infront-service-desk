from django.urls import path
from administrator import views
from . import views

urlpatterns = [
    path("users", views.users, name="users"),
    path("users/<str:pk>", views.update_modal, name="update_modal"),
    path("update_user/<str:pk>", views.update_user, name="update_user"),
    
    path("delete_user_modal/<str:pk>", views.delete_user_modal, name="delete_user_modal"),
    path("delete_user/<str:pk>", views.delete_user, name="delete_user"),

    path("groups", views.groups, name="groups"),
    path("create_group", views.create_group, name="create_group"),
    path("group_create_modal", views.group_create_modal, name="group_create_modal"),
    path("groups/<str:pk>", views.update_modal, name="update_modal"),
    path("delete_technician/<str:pk>", views.delete_technician, name="delete_technician"),
    path("delete_technician_modal/<str:pk>", views.delete_technician_modal, name="delete_technician_modal"),

    path("companies", views.companies, name="companies"),
    path("update_company/<str:pk>", views.update_company, name="update_company"),
    path("companies/<str:pk>", views.update_company_modal, name="update_company_modal"),
    path("delete_company_modal/<str:pk>", views.delete_company_modal, name="delete_company_modal"),
    path("delete_company/<str:pk>", views.delete_company, name="delete_company"),

]
