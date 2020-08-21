from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 

class Note(models.Model):
    title = models.CharField(max_length = 30, blank=False)
    body = models.TextField(blank=False)
    # image_upload = models.ImageField(upload_to='media/', blank=True)
    # file_upload = models.FileField(upload_to='media/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    public = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title 

    class Meta: 
        ordering = ['-date_posted',]


