from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.http  import HttpResponse
from django.urls import reverse


@login_required
def home(request):

    return HttpResponse('my project')




def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
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
