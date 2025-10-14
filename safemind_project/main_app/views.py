from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import JournalEntryForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from django.urls import reverse
from .models import TipReminder
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import JournalEntry
import random

def about(request):
    return render(request,'main_app/about.html')


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    
    return render(request, 'main_app/index.html', {'form': form})
"""""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    error_message = None

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')  # get email from POST

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            error_message = "Email already taken"
        elif form.is_valid():
            user = form.save(commit=False)  # don't save yet
            user.email = email  # set email
            user.save()  # now save to DB
            login(request, user)
            return redirect('home')
        else:
            error_message = "Please correct the errors below."
    else:
        form = UserCreationForm()

    return render(request, 'main_app/signup.html', {
        'form': form,
        'error_message': error_message
    })"""""


def signup(request):
    error_message = None  # optional: to pass to template
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST.get('email') # we added user's email
            user = form.save()  # saves user to DB
            login(request, user)  # log the user in
            return redirect('home')
        else:
            error_message = "Please correct the errors below."
    else:
        form = UserCreationForm()  # make sure form is always defined

    return render(request, 'main_app/signup.html', {
        'form': form,
        'error_message': error_message
    })

"""
from .models import JournalEntry
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    journals = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main_app/home.html', {'journals': journals})"""


@login_required
def home(request):
    # Get only journals for the current logged-in user
    journals = JournalEntry.objects.filter(user=request.user).order_by('created_at')
    #tips = TipReminder.objects.first()
   # tips = TipReminder.objects.all().order_by('-created_at')[:5]  # show latest 5 notes
    tips = list(TipReminder.objects.all())
    tip = random.choice(tips) if tips else None
    return render(request, "main_app/home.html", {"journals": journals, "tip": tip})
 

@login_required
def journal_detail(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    return render(request, 'journals/journal_detail.html', {'journal': journal})





@login_required
def journal_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            form.save_m2m()  # important for ManyToMany moods || saves the many to many relationship in the db 
            return redirect('journal_detail', pk=journal.pk)
    else:
        form = JournalEntryForm()
    return render(request, 'journals/journal_create.html', {'form': form})

@login_required
def journal_update(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES, instance=journal)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            form.save_m2m()  # save ManyToMany moods
            return redirect('journal_detail', pk=journal.pk)
    else:
        form = JournalEntryForm(instance=journal)
    return render(request, 'journals/journal_update.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import JournalEntry

@login_required
def journal_delete(request, pk):
    journal = get_object_or_404(JournalEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        journal.delete()
        return redirect('home')  

    
    return render(request, 'journals/journal_confirm_delete.html', {'journal': journal})


#Profile: 
@login_required
def profile(request):
    user = request.user  # current logged-in user
    return render(request, 'main_app/profile.html', {'user': user})

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # save the new password
            update_session_auth_hash(request, user)  # keep user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile') 
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'profiles/change_password.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)  
        user.delete()    
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('index') 
    return redirect('profile')  # fallback
