from django import forms
from .models import JournalEntry, Mood

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'journal','image', 'moods']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'journal': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'moods': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }