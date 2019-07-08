from django.shortcuts import render

def home(request):
    return render(request, 'softmain/index.html')
