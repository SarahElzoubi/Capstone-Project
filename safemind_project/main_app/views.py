from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate


def home(request):
    return HttpResponse("heeey")


def about(request):
    return render(request,'about.html')


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


def signup(request):
    error_message = None  # optional: to pass to template
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
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