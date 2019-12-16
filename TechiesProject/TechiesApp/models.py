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
programming_language_choices = (
    ('Python', 'Python'),
    ('Javascript', 'Javascript'),
    ('Java', 'Java'),
    ('HTML', 'HTML'),
    ('C Programming Language', 'C Programming Language'),
    ('CSS', 'CSS'),
    ('Django', 'Django'),
    ('ReactJS', 'ReactJS'),
    ('React Native', 'React Native'),
    ('Swift', 'Swift'),
    ('SQL', 'SQL'),
    ('Ruby', 'Ruby'),
    ('Node.JS', 'Node.JS'),
    ('UI/UX', 'UI/UX')
)


class CustomUser(AbstractUser):
    pass
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_image = models.ImageField(upload_to='media', null=True, blank=True)
    email = models.EmailField(max_length=254, verbose_name="Email", unique=True)
    username = models.CharField(max_length=60, unique=True)
    age_group = models.CharField(max_length=50, choices=age_choices, default="Youth")
    skill_level = models.CharField(max_length=50, choices=skill_choices, default="Newbie")
    tech_experience = models.CharField(max_length=50, choices=tech_experience_choices, default="Education")
    password = models.CharField(max_length=15, verbose_name="Password", unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.username} {self.age_group} {self.skill_level}" \
               f" {self.tech_experience} {self.password}"


class Event(models.Model):
    event_name = models.CharField(max_length=600)
    location = models.CharField(max_length=600)
    event_image = models.ImageField(upload_to='media', null=True, blank=True)
    description = models.CharField(max_length=6000)
    event_skill_level = models.CharField(max_length=60, choices=skill_choices)
    event_age_group = models.CharField(max_length=50, choices=age_choices)
    programming_language = models.CharField(max_length=60, choices=programming_language_choices)
    event_category = models.CharField(max_length=60, choices=tech_experience_choices)

    def __str__(self):
        return f"{self.event_name} {self.location} {self.event_image} {self.description} " \
               f"{self.event_age_group} {self.programming_language} {self.event_category}"
