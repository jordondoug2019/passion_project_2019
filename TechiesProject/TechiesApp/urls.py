from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='logIn'),
    path('sign_up', views.signup, name='signUp'),
    path('home/', views.home, name='home'),
    path('user_profile/<int:user_id>/', views.userprofile, name='user_profile'),
    path('event/<int:number>/', views.eventdisplay, name='event_display'),
    path('logout/', views.logOut, name='logOut')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
