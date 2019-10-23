# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.SignUp.as_view(), name='home'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
]