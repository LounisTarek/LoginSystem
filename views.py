from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username1']
        email = request.POST['email1']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "username already exists")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "password didn't match!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "your account has been successefully creates")
        return redirect('signin')

    return render(request ,'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username = username,password = pass1)

        if user is not None:
            login(request, user)
            return render(request, "index.html",{'username':username})

        else:
            messages.error(request, "check username or password")
            return redirect('signin')

    return render(request ,'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('signin')

