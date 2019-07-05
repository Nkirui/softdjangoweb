from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.http  import HttpResponse
from django.urls import reverse


# Create your views here.
@login_required
def home(request):
    return render(request, 'cbsapp/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
