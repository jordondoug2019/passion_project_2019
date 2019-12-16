from django.forms import ModelForm
from .models import CustomUser, Event


class UserRegistration(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'age_group', 'skill_level', 'tech_experience',
                  'password']


class UserLogin(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class UserProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'user_image', 'password']
