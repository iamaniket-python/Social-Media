from django.shortcuts import render,redirect
from django.contrib.auth.models import User,User
from .models import Userprofile
from django.contrib.auth import authenticate,login
# Create your views here.
def singup(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            User= User.objects.create_user(name,email,password)
            User.save()
            User_model = User.objects.get(username=name)
            new_profile = Userprofile.objects.create(User=User_model,id_user=User_model.id)
            new_profile.save()
            if User is not None:
                login(request,User)
                return redirect('/')
            return redirect('/login')
    except:
        invalid="Username already exist"
        return render(request,'singup.html',{"invalid":invalid})
        pass
    return render(request, 'singup.html')

def loginn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, User)
            return redirect('/')
        invalid="Invalid username or password"
        return render(request, 'login.html',{"invalid":invalid})
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')