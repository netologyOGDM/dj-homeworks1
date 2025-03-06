#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#Основной urls.py проекта (first_project/urls.py):

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

#2. URL-маршруты приложения app (app/urls.py):
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('current_time/', views.current_time_view, name='current_time'),
    path('workdir/', views.workdir_view, name='workdir'),
]

#3. Представления в app/views.py:
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os

def home_view(request):
    return render(request, 'home.html')

def current_time_view(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current Time: {current_time}")

def workdir_view(request):
    files = os.listdir()
    files_list = "<br>".join(files)
    return HttpResponse(f"Contents of the working directory:<br>{files_list}")