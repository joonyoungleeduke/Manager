from django.contrib import admin
from django.urls import path, include
from . import views as notes_views
from django.conf.urls import url 
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('notes/', notes_views.notes, name="notes-home"),
    path('note-create/', notes_views.new_note, name="notes-create"),
    path('note-delete/<int:id>/', notes_views.delete_note, name='notes-delete'),
    path('home/<int:id>', notes_views.notes, name='notes-edit'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)