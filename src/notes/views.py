from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator 
from .forms import NoteForm
from django.views.generic.base import View 

@login_required 
def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('notes-home')

@login_required
def notes(request, id=None):
    notes = Note.objects.filter(author=request.user) 
    paginator = Paginator(notes, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    if id != None: 
        note = Note.objects.get(id=id)
        if request.method == "POST":
            editNote = NoteForm(request.POST, author=request.user)
            if editNote.is_valid():
                note.delete()
                editNote.save() 
                return redirect('notes-home')
        else: 
            editNote = NoteForm(author=request.user, instance=note)

        context = {'page_obj':page_obj,
            'noteform': editNote,
            'author':request.user,
            'id': id}

    else: 
        if request.method == "POST":
            newNote = NoteForm(request.POST, author=request.user)
            if newNote.is_valid():
                newNote.save() 
                return redirect('notes-home')
        else: 
            newNote = NoteForm(author=request.user)

        context = {'page_obj':page_obj,
                'noteform': newNote,
                'author':request.user}

    return render(request, 'notes/notes.html', context) 

@login_required
def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, author=request.user)
        if form.is_valid():
            form = form.save() 
            return redirect('notes-home')
    else: 
        form = NoteForm(author=request.user) 
    return render(request, 'notes/notes.html', {'form':form})