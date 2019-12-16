from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
age_choices = (
    ('Youth', '17 and Younger'),
    ('Young Adult', '18-25'),
    ('Adult', '26+')
)

skill_choices = (
    ('Newbie', '2 years or less'),
    ('Intermediate', '3-5 years'),
    ('Experienced', '5+')
)
tech_experience_choices = (
    ('Education', 'Education'),
    ('Social', 'Social'),
    ('Conference', 'Conference'),
    ('Special Events', 'Special Events'),
    ('Youth Programs', 'Youth Programs')
)


class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, verbose_name="Email" , unique=True)
    username = models.CharField(max_length=60)
    age_group = models.CharField(max_length=50, choices=age_choices, default="Youth")
    skill_level = models.CharField(max_length=50, choices=skill_choices, default="Newbie")
    tech_experience = models.CharField(max_length=50, choices=tech_experience_choices, default="Education")
    password = models.CharField(max_length=15, verbose_name="Password", unique=True)