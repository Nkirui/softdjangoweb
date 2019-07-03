from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import SignupForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls  import reverse


# Create your views here.
@login_required()
def index(request):
    return render(request, 'cbsapp/index.html')


def register(request):
    '''
    registration function
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = SignupForm()

    return render(request, 'registration/registration_form.html', {'form': form})


def profile(request, username):
    '''
    function that returns user profile
    '''
    title = "Profile"
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)
    id = request.user.id
    form = ProfileForm()

    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)

    return render(request, 'registration/profile.html', {'title':title,'form':form,'profile':profile,'profile_info':profile_info})




@login_required()
def update_profile(request):
    '''
    function that updtates user profile
    '''

    profile = User.objects.get(username=request.user)
    try :
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)

    if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                update = form.save(commit=False)
                update.user = request.user
                update.save()
                messages.success(request,"Profile Updated")
                return redirect('profile', username=request.user)
    else:
        form = ProfileForm()

    return render(request, 'registration/updateProfile.html', {'form':form, 'profile_info':profile_info})
