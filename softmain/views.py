from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        email_form = EmailForm(data=request.POST)
        if email_form.is_valid():
            sender = email_form.cleaned_data['email']
            subject = email_form.cleaned_data['subject']
            message = email_form.cleaned_data['message']
            send_mail(subject, message, sender, ['nathankirui5@gmail.com'])
            email_form.save()
            messages.success(request, 'Sent successfully')
    else:
        email_form = EmailForm()
    return render(request, 'softmain/index.html', {'email_form': email_form})
