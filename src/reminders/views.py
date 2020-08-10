from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt

@login_required
def reminders(request):
    reminders = Reminder.objects.filter(author=request.user)

    context = {'reminders':reminders}

    return render(request, 'reminders/reminders.html', context)

@login_required
@csrf_exempt
def add_reminder(request):
    if request.method == 'POST':
        content = request.POST['reminder_content']
        new_reminder = Reminder(title=content, author=request.user)
        new_reminder.save()
        return redirect('reminders-main')
    else:
        return redirect('reminders-main')

@login_required 
@csrf_exempt
def delete_reminder(request):
    if request.method == 'POST':
        id = request.POST['id']
        reminder = get_object_or_404(Reminder, id=id)
        reminder.delete() 
    return redirect('reminders-main')