from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    
   
    # path('rates', views.apps1,name='rates'),
    
    path('codeapp', views.codeapp,name='codeapp'),
    path('code_page',views.code_page,name='code_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)