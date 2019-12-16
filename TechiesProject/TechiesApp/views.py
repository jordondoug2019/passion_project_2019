from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import CustomUser, Event
from .forms import UserRegistration, UserProfileForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def index(request):
    if request.method == 'POST':
        user_login = authenticate(email=request.post["email"], password=request.post["password"])
        if user_login is not None:
            return redirect('TechiesApp/index.html')
        else:
            messages.error(request, "Email or Password is incorrect")
        return redirect('logIn')
    context = {
        'loginForm': UserRegistration
    }
    return render(request, 'TechiesApp/home.html', context)


def signup(request):
    if request.method == 'POST':
        user_signup = UserRegistration(request.post or None)
        if user_signup.is_valid():
            user_signup = CustomUser.objects.create_user(first_name=request.post['first_name'],
                                                         last_name=request.post['last_name'],
                                                         username=request.post['username'],
                                                         email=request.post['email'],
                                                         age_group=request.post['age_group'],
                                                         skill_level=request.post['skill_level'],
                                                         tech_experience=request.post['tech_experience'],
                                                         password=request.post['password'])
            login(request, user_signup)
            return redirect('home')
        else:
           messages.error(request, "")
            return render(request, 'TechiesApp/signup.html', context)
