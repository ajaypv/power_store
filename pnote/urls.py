from django.urls import path
from .import views
from django.urls import re_path
urlpatterns =[
    
   
    # path('rates', views.apps1,name='rates'),
    
    path('note', views.note_app,name='note'),
    path('snote', views.note_share,name='snote'),
    path('noted/<str:pk>/',views.noted, name='dnote'),
    re_path(r'^like/$' , views.likeNote,name="likeNote"),
    
   
]
