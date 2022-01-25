from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class photos(models.Model):
    img = models.TextField()
    caption= models.CharField(max_length=225,null=True, blank=True)
    likes = models.IntegerField(default=0,null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    
    
class user_apps(models.Model):
    creater_name = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    programing_language = models.CharField(max_length=255, null=True, blank=True)
    app_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    code =models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    