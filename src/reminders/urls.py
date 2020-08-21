from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from django.conf.urls.static import static 
from django.conf import settings 
from . import views as reminders_views

urlpatterns = [
    path('reminders/', reminders_views.reminders, name="reminders-main"),
    path('reminder-add/', reminders_views.add_reminder, name="reminders-add"),
    path('reminder-delete/', reminders_views.delete_reminder, name='reminder-delete'),
]