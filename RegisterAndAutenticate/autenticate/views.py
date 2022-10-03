from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from .forms import CreateUser

from devtools import debug

def register(request):
    
    
    form  = CreateUser()
    
    if request.method == "POST":
        form = CreateUser(request.POST)
        # form.errors
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'User Created Succesfuly')
            redirect('base:users')
        
    
    return render(request, 'register/register.html', {"form" : form})

def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('base:users')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password = password)
    
        if user is not None:
            login(request, user)
            return redirect('base:users')
    
        else:
            messages.warning(request, 'User or Password is INCORRECT')
    
    return render(request, 'register/login.html')

def log_out(request):
    logout(request)
    return redirect('auth:login')