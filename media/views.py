from rest_framework import viewsets,status
import datetime 
from django.utils import timezone
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serilaizer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer