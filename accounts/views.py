
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user =auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            return redirect('home')
        else:
            return render(request,'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')
