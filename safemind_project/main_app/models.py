from django.db import models
from django.contrib.auth.models import User;

from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Jornal_entries")
    title=models.CharField(max_length=200)
    journal=models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    created_at=models.DateTimeField(auto_now_add=True)
