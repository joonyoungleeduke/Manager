from django.db import models
from django.utils import timezone 
from users import models as users_models 

class Reminder(models.Model):
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(users_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta: 
        ordering = ['-date_posted',]