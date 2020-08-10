from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from users import views as user_views
from . import views as main_views

urlpatterns = [
    path('', main_views.landing, name="main-landing"),
]
