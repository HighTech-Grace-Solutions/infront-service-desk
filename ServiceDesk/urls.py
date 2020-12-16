"""ServiceDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('comments/', include('django_comments_xtd.urls')),
    path('',include("iam.urls")),
    path("ticket/", include("incident_management.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("administrator/", include('administrator.urls')),
    path('account/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('home/', include('landing_page.urls')),
    path('SLA/', include('SLA.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)