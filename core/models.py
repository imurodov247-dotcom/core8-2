from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    title = models.CharField()
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner  = models.ForeignKey(User,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.title} by {self.owner}"