# project_name/urls.py
from django.contrib import admin
from django.urls import path
from app import views  # Импортируем view-функции из приложения app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Домашняя страница
    path('current_time/', views.current_time_view, name='current_time'),  # Текущее время
    path('workdir/', views.workdir_view, name='workdir'),  # Содержимое рабочей директории
]