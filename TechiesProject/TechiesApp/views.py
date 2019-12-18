from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import User, Event
from .forms import UserRegistration, UserProfileForm, UserLogin
from django.contrib.auth import login, logout, authenticate, get_user_model


# Create your views here.

def index(request):
    if request.method == 'POST':
        user_login = authenticate(username=request.POST['username'], password=request.POST["password"])
        if user_login is not None:
            login(request, user_login)
            print('logged in')
            return redirect('home')
        else:
            messages.error(request, "Email or Password is incorrect")
            return redirect('logIn')
    context = {
        'loginForm': UserLogin
    }
    return render(request, 'TechiesApp/index.html', context)


def signup(request):
    if request.method == 'POST':
        user_signup = UserRegistration(request.POST or None)
        if user_signup.is_valid():
            user_signup = User.objects.create_user(first_name=request.POST['first_name'],
                                                   last_name=request.POST['last_name'],
                                                   username=request.POST['username'],
                                                   email=request.POST['email'],
                                                   age_group=request.POST['age_group'],
                                                   skill_level=request.POST['skill_level'],
                                                   tech_experience=request.POST['tech_experience'],
                                                   password=request.POST['password'])
            login(request, user_signup)
            return redirect('home')
        else:
            messages.error(request, "Information already Exist!")
            return redirect('signUp')
    context = {
        'UserRegistration': UserRegistration
    }
    return render(request, 'TechiesApp/signUp.html', context)


def home(request):
    if request.user.is_authenticated:
        if User.age_group == 'Youth':
            Event.event_age_group.filter('Youth')
        if User.age_group == 'Young Adult':
            Event.event_age_group.filter('Young Adult')
        if User.age_group == 'Adult':
            Event.event_age_group.filter('Adult')
        if User.skill_level == 'Newbie':
            Event.event_skill_level.filter('Newbie')
        if User.skill_level == "Intermediate":
            Event.event_skill_level.filter('Intermediate')
        if User.skill_level == "Experienced":
            Event.event_skill_level.filter('Experienced')
        if User.tech_experience == 'Education':
            Event.event_category.filter("Education")
        if User.tech_experience == 'Social':
            Event.event_category.filter("Social")
        if User.tech_experience == 'Conference':
            Event.event_category.filter("Conference")
        if User.tech_experience == 'Special Events':
            Event.event_category.filter('Special Events')
        if User.tech_experience == 'Youth Programs':
            Event.event_category.filter('Youth Programs ')
    context = {
        'YouthAgeGroupChoices': Event.event_age_group == 'Youth',
        'YoungAdultAgeGroupChoices': Event.event_age_group == 'Young Adult',
        'AdultAgeGroupChoices': Event.event_age_group == 'Adult',
        'NewbieSkillChoices': Event.event_skill_level == 'Newbie',
        'IntermediateSkillChoices': Event.event_skill_level == 'Intermediate',
        'ExperiencedSkillChoices': Event.event_skill_level == 'Experienced',
        'EducationChoices': Event.event_category == "Education",
        'SocialChoices': Event.event_category == "Social",
        'ConferenceChoices': Event.event_category == "Conference",
        'YouthProgramChoices': Event.event_category == 'Youth Programs '
    }
    return render(request, 'TechiesApp/home.html', context)


def userprofile(request, user_id):
    each_user_profile = get_object_or_404(UserRegistration, pk=user_id)
    pre_fill_form = UserProfileForm(request.POST or None, request.FILES, instance=each_user_profile)
    if request.method == "POST":
        if pre_fill_form.is_valid():
            pre_fill_form.save()
        return redirect('home')
    context = {
        'userprofileForm': UserProfileForm(instance=each_user_profile)
    }
    return render(request, 'TechiesApp/user_profile.html', context)


def eventdisplay(request, number):
    eventID = get_object_or_404(Event, pk=number)
    context = {
        'event': eventID,
        'Event': Event.objects.filter(pk=eventID)
    }
    return render(request, 'TechiesApp/event_display.html', context)


def logOut(request):
    logout(request)
    return redirect('logIn')
