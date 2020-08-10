from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 
from .models import Profile 
from django.views.generic.edit import UpdateView

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users-login")
    else:
        form = RegisterForm() 

    return render(request, 'users/register.html', {'form': form})

@login_required 
def profile(request, owner):

    return render(request, 'users/profile.html', {'owner': request.user.username,})