from datetime import datetime, timedelta
from django.conf import settings
from rest_framework import serializers
import random
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(
    write_only=True,
    min_length=settings.MIN_PASSWORD_LENGTH
    error_message={
        min_length: f"Password should be at least {settings.MIN_PASSWORD_LENGTH}characters"
    },
)
    password2=serializers.CharField(
    write_only=True,
    min_length=settings.MIN_PASSWORD_LENGTH
    error_message={
        min_length: f"Password should be at least {settings.MIN_PASSWORD_LENGTH}characters"
    },
)
    
    class meta:
        model=User
        fields=['phone_number','email','password1','password2']

    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password does not match")
        return data
    
    def create(self,validated_data):
        otp=random.randint(1000,9999)
        otp_expriy=datetime.now()+ timedelta(minutes=3)

        user=User(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            otp=otp,
            otp_expriy=otp_expriy,
            max_otp_tyr=settings.MAX_OTP_TRY,
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user