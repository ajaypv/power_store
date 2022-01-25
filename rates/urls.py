from django.urls import path
from .import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    
   
    
    path('rates', views.apps1, name='rates'),
    path('prof', views.profile2,name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)