from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, FormView
from django.db import models
from .models import Profile, Post
from .forms import ProfileForm, PostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

import time
# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import datetime


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PostSubmission(FormView):
    template_name = "vibbo/post_submit.html"
    form_class = PostForm

    def get_initial(self):
        return {
            'title': "",
            'body': ""
        }

    def get_queryset(self):
        return Post(user=self.request.user)

    def form_valid(self, form):
        data = form.cleaned_data
        post = self.get_queryset()

        post.title = data['title']
        post.body = data['body']

        post.date = datetime.datetime.now()

        post.save()
        print(post)
        return HttpResponseRedirect(f"/vibbo/post/{post.pk}/")


class ChangePostView(FormView):
    template_name = 'vibbo/post_submit.html'
    form_class = PostForm

    def get_initial(self):
        return {
            'title': self.get_queryset().title,
            'body': self.get_queryset().body
        }

    def get_queryset(self):
        return Post.objects.get(pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        post = self.get_queryset()

        data = form.cleaned_data

        post.title = data['title']
        post.body = data['body']

        post.date = datetime.datetime.now()

        post.save()
        print(post)
        return HttpResponseRedirect(f"/vibbo/post/{post.pk}/")


class ChangeProfileView(FormView):
    template_name = 'vibbo/profile_change.html'
    form_class = ProfileForm

    def get_initial(self):
        return {
            'first_name': self.request.user.profile.first_name,
            'last_name': self.request.user.profile.last_name,

            'bio': self.request.user.profile.bio,

            'street': self.request.user.profile.street,
            'city': self.request.user.profile.city,
            'location_code': self.request.user.profile.location_code
        }

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):

        data = form.cleaned_data
        profile = self.get_queryset()

        profile.first_name = data['first_name']
        profile.last_name = data['last_name']

        profile.bio = data['bio']

        profile.street = data['street']
        profile.city = data['city']
        profile.location_code = data['location_code']

        profile.save()

        # return HttpResponse('ok')
        return HttpResponseRedirect(f"/vibbo/profile/{self.request.user.profile.pk}/")


class DisplayDetailView(DetailView):
    template_name = "vibbo/profile_page.html"
    model = Profile


class PostView(DetailView):
    template_name = "vibbo/post_page.html"
    model = Post


def allUsers(request, pk=None):
    users = User.objects.all()
    template_name = "vibbo/allUsers.html"

    first_names = []
    name_user_searched = ""

    for user in users:
        first_names.append(user.username)

    if pk is None:
        context = {
            'users': first_names,
        }
    else:
        for name in first_names:
            if name == pk:
                name_user_searched = name
        context = {
            'users': first_names,
            'user_searched': name_user_searched,
        }

    return render(request, template_name, context)


def all_posts(request):
    posts = Post.objects.filter(user=request.user).order_by('-date')
    template_name = 'vibbo/all_posts.html'

    context = {
        'user': request.user,
        'posts': posts
    }

    return render(request, template_name, context)


def delete_post(request, pk, **kwargs):
    post = Post.objects.get(pk=pk)
    post.delete()

    return HttpResponseRedirect(f"../delete/success")


def followUser(request, id):
    from_user = get_object_or_404(User, id=id)
    from_user.profile.follows.add(request.user.profile)
    return HttpResponseRedirect(f"/vibbo/home/allusers")


def unfollowUser(request, id):
    from_user = get_object_or_404(User, id=id)
    from_user.profile.follows.remove(request.user.profile)
    return HttpResponseRedirect(f"/vibbo/home/allusers")


def getAllMyFollowsPosts(request):
    all_following_posts = Post.objects.filter(user=request.user)
    template_name = 'vibbo/all_posts.html'

    for following in request.user.profile.follows.all():
        posts = Post.objects.filter(user=following).order_by('-date')
        for post in posts:
            all_following_posts.append(post)

    context = {
        'user': request.user,
        'posts': all_following_posts
    }

    return render(request, template_name, context)
