from django.shortcuts import render
import datetime
import requests 
from random import choice


def landing(request): 
    context = {}
    return render(request, 'main/landing.html', context)