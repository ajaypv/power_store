from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class note(models.Model):
    creater_name = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    notebook = models.CharField(max_length=255, null=True, blank=True)
    about = models.CharField(max_length=255)
    link = models.TextField(null=True, blank=True)
    stars =models.ManyToManyField(User,related_name="note_stars",blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    like_count= models.IntegerField(null=True, blank=True)

    def totalLikes(self):
        return self.stars.count()

