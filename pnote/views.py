from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import note
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import reverse_lazy, reverse
# Create your views here.
from twilio.rest import Client 
 
account_sid = 'ACbf4e15b0761d5fb1db4f9efcbf576cb8' 
auth_token = '8ce2161a9ae42bad4fe753cbdb6dfceb' 




def note_app(request):
    notes = note.objects.all()
   
    context = {'notes':notes}
    return render(request, 'pnote.html',context)


def note_share(request):

    try:
        user = request.user
        note_name = request.POST.get('note_name')
        noteabout= request.POST.get('anote')
        link = request.POST.get('link')
        first_link = link.index('https')
        true_point = link.index('true')
        slink = link[first_link:true_point+4]
        notes = note()
        notes.creater_name = user
        notes.notebook = note_name
        notes.about = noteabout
        notes.link = slink
        notes.like_count =0
        notes.save()
    except:
        print("error")
    
    return render(request, 'snote.html')


def noted(request,pk):
    note1 = note.objects.get(id =pk)
    print(note1.totalLikes())
    liked = False 
    if note1.stars.filter(id=request.user.id).exists():
        liked = True

    context = {'note1':note1,'liked':liked ,} 
    return render(request, 'snotepage.html',context)


def likeNote(request):
    id = request.POST.get('note_id')
    
    note2 = note.objects.get(id=id)
    liked = False
    lcount = int(note2.like_count)
    if note2.stars.filter(id=request.user.id).exists():
        note2.stars.remove(request.user)
        liked =False
        if lcount ==0:
            lcount -=1
            note2.like_count = lcount
            note2.save()   
    else:
        note2.stars.add(request.user)
        liked = True
        lcount +=1
        note2.like_count = lcount
        note2.save()


        
    return HttpResponseRedirect(reverse('dnote', args =[str(id)]))
