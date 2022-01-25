from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
# from .models import pic
import  messagebird
import pyrebase
from django.contrib.auth.decorators import login_required
from main.models import photos
# Create your views here.
config = {
 "apiKey": "AIzaSyD2o880tOwmj1ajkjjRDUpuqwFfbwlGrMY",
  "authDomain": "webrtc-d80ed.firebaseapp.com",
  "databaseURL": "https://webrtc-d80ed-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "webrtc-d80ed",
  "storageBucket": "webrtc-d80ed.appspot.com",
  "messagingSenderId": "139243151056",
  "appId": "1:139243151056:web:15b4977cdf1d4346c788d5",
  "measurementId": "G-Y4630Q7FYB"
}

context1 ={}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
auth = firebase.auth()


emailAddress ="ajajaoefn@gmail.com"


def apps1(request):
    posts1 = photos.objects.all().count()
    a = posts1/3
    phot1 = photos.objects.all().order_by('-likes')[a:a+a]
    phot3 = photos.objects.all().order_by('-likes')[a+a-1:]
    phot = photos.objects.all().order_by('-likes')[:a]
    posts = photos.objects.all()    
    context = {'img':phot1, 'img2':phot, 'img3':phot3}
    if request.method=='POST':
        print("ourehgoewbghowei")
        posted=request.POST.get("post")
        pos =  int(float(posted))
        print('ruhgaoregbhaoeuwbgjihgworgbweogbo')
        print(posted)
        for post in posts:
            if (int(post.id)==int(pos)):
                post.likes+=1
                print(post.likes)
                post.save()
    
        # return redirect('rates')
    return render(request,'rates1.html',context)


def profile2(request):
     current_user = request.user
     userid = current_user.id
     posts1 = photos.objects.filter(user_id=2).all()
     phot = { 'id': posts1}
     
     if request.method == 'POST':
         uploaded_file = request.FILES.get('document')
         fs = FileSystemStorage()
         name = fs.save(uploaded_file.name, uploaded_file)
         fn= 'media'+"\\"+name
         a= fs.url(name)
         print(name)
         print(a)
         pho= photos()
         pho.img=a
         pho.likes=0
         pho.caption= request.POST.get('caption')
         pho.user_id= userid
         
         pho.save()
     return render(request,'pic_uplod.html',phot)