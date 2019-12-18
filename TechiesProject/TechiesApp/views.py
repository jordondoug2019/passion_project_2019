from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Event
from .forms import UserRegistration, UserProfileForm, UserLogin
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your views here.

def index(request):
    if request.method == 'POST':
        user_login = authenticate(username=request.POST['username'], password=request.POST["password"])
        if user_login is not None:
            login(request, user_login)
            print(User.objects.tech_experience)
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
        if User.objects.filter(age_group="Youth"):
            Event.objects.filter(event_age_group='Youth')
        if User.objects.filter(age_group="Young Adult"):
            Event.objects.filter(event_age_group='Young Adult')
        if User.objects.filter(age_group='Adult'):
            Event.objects.filter(event_age_group='Adult')
        if User.objects.filter(age_group="All Ages"):
            Event.objects.filter(event_age_group="All Ages")
        if User.objects.filter(skill_level="Newbie"):
            Event.objects.filter(event_skill_level='Newbie')
        if User.objects.filter(skill_level="Intermediate"):
            Event.objects.filter(event_skill_level='Intermediate')
        if User.objects.filter(skill_level="Experienced"):
            Event.objects.filter(event_skill_level='Experienced')
        if User.objects.filter(tech_experience="Education"):
            Event.objects.filter(event_category="Education")
        if User.objects.filter(tech_experience='Social'):
            Event.objects.filter(event_category="Social")
        if User.objects.filter(tech_experience="Conference"):
            Event.objects.filter(event_category="Conference")
        if User.objects.filter(tech_experience='Special Events'):
            Event.objects.filter(event_category='Special Events')
        if User.objects.filter(tech_experience="Youth Programs"):
            Event.objects.filter(event_category='Youth Programs ')
    context = {
        'YouthAgeGroupChoices': Event.objects.filter(event_age_group='Youth'),
        'YoungAdultAgeGroupChoices': Event.objects.filter(event_age_group='Young Adult'),
        'AdultAgeGroupChoices': Event.objects.filter(event_age_group='Adult'),
        'NewbieSkillChoices': Event.objects.filter(event_skill_level='Newbie'),
        'IntermediateSkillChoices': Event.objects.filter(event_skill_level='Intermediate'),
        'ExperiencedSkillChoices': Event.objects.filter(event_skill_level='Experienced'),
        'EducationChoices': Event.objects.filter(event_category="Education"),
        'SocialChoices': Event.objects.filter(event_category="Social"),
        'ConferenceChoices': Event.objects.filter(event_category="Conference"),
        'YouthProgramChoices': Event.objects.filter(event_category='Youth Programs ')
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
