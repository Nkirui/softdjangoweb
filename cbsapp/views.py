from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

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

    return render(request, 'registration/profile.html', {'title':title,'form':form,'profile_info':profile_info})




@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method =='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            task.save()
            messages.success(request,'profile created successfuly')
        return redirect('profile')
    else:
        form = ProfileForm()
        return render(request,'reegistration/newProfile.html',{"form":form})



def update_profile(request,pk):
    profile = get_object_or_404(Profile,pk=pk)
    if request == 'POST':
        form = ProfileForm(request.POST, instance = profile)
        try :
            if form.is_valid():
                profile = form(commit=False)
                profile.save()
                messages.success('your profile is updated')
                return redirect(home)
        except Exception as e:
            HttpResponse(request, 'profile not updated')
    else :
        form = ProfileForm(instance=profile)
        return render(request, 'registration/newProfile.html',{'profile':profile,'form':form})
