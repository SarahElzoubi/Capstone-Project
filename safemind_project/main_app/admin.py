from django.contrib import admin

from .models import JournalEntry , Mood
admin.site.register(JournalEntry)
admin.site.register(Mood)
