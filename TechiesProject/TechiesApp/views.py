from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import CustomUser, Event
from .forms import UserRegistration, UserProfileForm, UserLogin
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def index(request):
    if request.method == 'POST':
        user_login = authenticate(email=request.POST["email"], password=request.POST["password"])
        if user_login is not None:
            return redirect('logIn')
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
            user_signup = CustomUser.objects.create_user(first_name=request.POST['first_name'],
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
    if UserRegistration.age_group.choices == 'Youth':
        Event.event_age_group.choices.filter('Youth')
    if UserRegistration.age_group.choices == 'Young Adult':
        Event.event_age_group.choices.filter('Young Adult')
    if UserRegistration.age_group.choices == 'Adult':
        Event.event_age_group.choices.filter('Adult')
    if UserRegistration.skill_level.choices == 'Newbie':
        Event.event_skill_level.choices.filter('Newbie')
    if UserRegistration.skill_level.choices == "Intermediate":
        Event.event_skill_level.choices.filter('Intermediate')
    if UserRegistration.skill_level.choices == "Experienced":
        Event.event_skill_level.choices.filter('Experienced')
    if UserRegistration.tech_experience.choices == 'Education':
        Event.event_category.choices.filter("Education")
    if UserRegistration.tech_experience.choices == 'Social':
        Event.event_category.choices.filter("Social")
    if UserRegistration.tech_experience.choices == 'Conference':
        Event.event_category.choices.filter("Conference")
    if UserRegistration.tech_experience.choices == 'Special Events':
        Event.event_category.choices.filter('Special Events')
    if UserRegistration.tech_experience.choices == 'Youth Programs':
        Event.event_category.choices.filter('Youth Programs ')
    context = {
        'YouthAgeGroupChoices': Event.event_age_group.choices.filter('Youth'),
        'YoungAdultAgeGroupChoices': Event.event_age_group.choices.filter('Young Adult'),
        'AdultAgeGroupChoices': Event.event_age_group.choices.filter('Adult'),
        'NewbieSkillChoices': Event.event_skill_level.choices.filter('Newbie'),
        'IntermediateSkillChoices': Event.event_skill_level.choices.filter('Intermediate'),
        'ExperiencedSkillChoices': Event.event_skill_level.choices.filter('Experienced'),
        'EducationChoices': Event.event_category.choices.filter("Education"),
        'SocialChoices': Event.event_category.choices.filter("Social"),
        'ConferenceChoices': Event.event_category.choices.filter("Conference"),
        'YouthProgramChoices': Event.event_category.choices.filter('Youth Programs ')
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
