from django.contrib import admin

from .models import JournalEntry , Mood , TipReminder
admin.site.register(JournalEntry)
admin.site.register(Mood)
admin.site.register(TipReminder)
