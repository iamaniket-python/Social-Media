from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator, validate_email

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
#OTP
class User(AbstractUser,PermissionsMixin):
    phone_number =models.CharField(unique=True,max_length=10,null=False,blank=False,validators=[phone_regex])
    email =models.EmailField(max_length=10,null=False,blank=False,validators=[validate_email])
    otp=models.CharField(max_length=4)
    otp_expriy=models.DateTimeField(blank=True,null=True)
    otp_max_out =models.DateTimeField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_regsitered = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'phone_number'
    
    objects = UserManager()

    def __str__(self):
        return self.phone_number

class UserManager(BaseUserManager):
    
    def create_user(self,phone_number,password=None):
        if phone_number is None:
            raise TypeError('User should have a phone number')
        if password is None:
            raise TypeError('User should have a password')
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone_number,password=None):
        if phone_number is None:
            raise TypeError('User should have a phone number')
        if password is None:
            raise TypeError('User should have a password')
        user = self.create_user(phone_number, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


















class Userprofile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True,default=0)
    bio=models.TextField(blank=True,default='')
    profileimg=models.ImageField(upload_to='profile_images',blank=True,default='No_image_available.svg.png')
    location=models.CharField(max_length=30,blank=True,default='')
    birth_date=models.DateField(null=True,blank=True)

def __str__(self):
    return self.name
