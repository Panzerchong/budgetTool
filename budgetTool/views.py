from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RateTable


def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"There was an error log in. Please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html',{})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out...")
    return redirect('home')

def rate_table(request):
    table=RateTable.objects.all()

    return messages.success(request,"it's ratetable\n")
