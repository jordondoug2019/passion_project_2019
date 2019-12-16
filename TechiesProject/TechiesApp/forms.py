from django.forms import ModelForm
from .models import CustomUser, Event


class UserRegistration(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'user_image', 'password']
