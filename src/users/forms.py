from django.db import models
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Profile
from django.forms import ModelForm 

class RegisterForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta: 
        model = User
        fields = ["name", "username", "email", "password1", "password2"]