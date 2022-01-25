from django.shortcuts import render,redirect
from .forms import user_apps_f
from .models import *
from main.models import user_apps

# Create your views here.
def codeapp(request):
    if request.method == 'POST':
        code = user_apps()
        code.creater_name =request.user
        code.programing_language = request.POST.get('pro_lang')
        code.app_name = request.POST.get('program_name')
        code.description = request.POST.get('description')
        code.code = request.POST.get('code')
        code.save()
        return redirect('code_page')

               
       

    return render(request,'codeapp.html',)


def code_page(request):
    codes1 = user_apps.objects.all()
    context = {'codes':codes1}
    return render(request,'code_page.html',context)

