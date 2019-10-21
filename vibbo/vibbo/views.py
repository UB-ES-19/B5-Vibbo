from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.db import models
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ChangeProfileView(FormView):
    template_name = 'vibbo/profile_change.html'
    form_class = ProfileForm
    # success_url = reverse_lazy('')

    def get_initial(self):
        return {
            'occupation': self.request.user.profile.occupation,
            'bio': self.request.user.profile.bio,
            'location': self.request.user.profile.location
        }

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):

        data = form.cleaned_data
        profile = self.get_queryset()
        profile.occupation = data['occupation']
        profile.location = data['location']
        profile.bio = data['bio']
        profile.save()

        # return HttpResponse('ok')
        return HttpResponseRedirect("/")


class DisplayDetailView(DetailView):
    model = Profile
