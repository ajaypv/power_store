from django.db import models

# Create your models here.


class photos(models.Model):
    img = models.TextField()
    likes = models.CharField(max_length=225)