from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    # company_owner = forms.CharField(max_length=200, help_text='Required')
    # contact = forms.CharField(max_length=200, help_text='Required')
    # location = forms.CharField(max_length=200, help_text='Required')
    # about_company = forms.CharField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
