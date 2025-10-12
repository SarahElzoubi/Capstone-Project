from django.db import models
from django.contrib.auth.models import User;

from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



class Mood(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.name
    
class JournalEntry(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Jornal_entries")
    title=models.CharField(max_length=200)
    journal=models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    created_at=models.DateTimeField(auto_now_add=True)
    moods = models.ManyToManyField(Mood, blank=True)

    def __str__(self):
        return self.title

