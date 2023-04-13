from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        #authenticate
        
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in...")
            return redirect('home')
        else:
            messages.success(request, "There was an error loggin in, Please try again later.")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {})

def registerUser(request):
    return render(request, 'register.html', {})
   

def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')