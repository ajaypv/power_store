from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
# Create your views here.

def profile(request):
    return render(request,'profile.html')
def apps(request):
    return render(request,'apps.html')
def mainpg(request):
    return render(request,'main.html')

