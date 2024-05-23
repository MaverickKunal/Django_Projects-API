from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


#Username/password for test user: kunal; Boeing15#
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check if user has entered correct credentials 
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
                login(request,user)
                return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    #return render(request, 'logout.html')
    return redirect("/login")
    
def activeuserslist(request):
    active_period = timezone.now() - timedelta(minutes=1)
    active_users = User.objects.filter(last_login__gt=active_period)
    #to find all the users registered
    # active_users = User.objects.filter(is_active=True)
    context = {
        'active_users' : active_users
    }
    return render(request, 'activeusers.html', context)