from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile, Event
from django.contrib.auth.models import User


class UserProfileline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileline,)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ()}),
    )


# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile, UserAdmin),
admin.site.register(Event)
