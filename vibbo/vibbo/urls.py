# accounts/urls.py
from django.urls import path, re_path
from .views import ChangeProfileView, DisplayDetailView
from . import views


urlpatterns = [
    path(r'profile/<int:pk>/', DisplayDetailView.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.SignUp.as_view(), name='home'),
    path('change/', ChangeProfileView.as_view(), name='change'),
]