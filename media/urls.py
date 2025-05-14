from django.urls import path,include
from . import views
from rest_framework import DefaultRouter

router =DefaultRouter()
router.register('user',views.UserViewSet,basename='user')

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginn,name='login'),
    path('singup',views.singup,name='singup'),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns+=router.urls