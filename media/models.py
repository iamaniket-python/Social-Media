from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True,default=0)
    bio=models.TextField(blank=True,default='')
    profileimg=models.ImageField(upload_to='profile_images',blank=True,default='No_image_available.svg.png')
    location=models.CharField(max_length=30,blank=True,default='')
    birth_date=models.DateField(null=True,blank=True)

def __str__(self):
    return self.name
