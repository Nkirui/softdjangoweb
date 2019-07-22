from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm, ProfileForm
from django.http  import HttpResponse
from .models import Profile
from django.contrib.auth import logout


# Create your views here.
def hom(request):
    return render(request, 'cbsapp/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'')
            return redirect('create_profile')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    current_user =  request.user
    profile = Profile.objects.filter(user=current_user)
    print(profile)
    return render(request, 'users/profile.html', {'profile':profile})

@login_required
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            profile.save()
        return redirect('hom')

    else:
        form = ProfileForm()
    return render(request, 'users/newProfile.html',{'form':form})

def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/update_profile.html', context)



def logout_view(request):
    logout(request)
    return  redirect('home')
