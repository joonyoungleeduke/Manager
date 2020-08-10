from django.db import models
from django.utils import timezone 
from users import models as users_models 

class Note(models.Model):
    title = models.CharField(max_length = 30, blank=False)
    body = models.TextField(blank=False)
    # image_upload = models.ImageField(upload_to='media/', blank=True)
    # file_upload = models.FileField(upload_to='media/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(users_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title 

    class Meta: 
        ordering = ['-date_posted',]


