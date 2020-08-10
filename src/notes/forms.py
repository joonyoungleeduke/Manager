from django.forms import ModelForm 
from .models import Note
from django.db import models
from django.utils import timezone 
from crispy_forms.helper import FormHelper

class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super(NoteForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['rows'] = 28

        instance = kwargs.get('instance', None)
        if instance: 
            self.fields['title'].initial = instance.title 
            self.fields['body'].initial = instance.body 
    class Meta: 
        model = Note 
        labels = {'title': '', 'body': ''}
        exclude = ('author','date_posted')

    def save(self):
        obj = super(NoteForm, self).save(commit=False)
        obj.author = self.author 
        obj.save() 
        return obj 