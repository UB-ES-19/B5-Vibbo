# accounts/urls.py
from django.urls import path, re_path
from .views import ChangeProfileView, DisplayDetailView, PostSubmission, ChangePostView, delete_post
from . import views
from .models import Post

from django.views.generic import TemplateView
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name="contacts"),
    path('home/', views.SignUp.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path(r'profile/<int:pk>/', DisplayDetailView.as_view(), name='profile'),
    path('change/', ChangeProfileView.as_view(), name='change'),

    path('home/allusers', views.allUsers, name='allusers'),
    path('home/allusers/<str:pk>/', views.allUsers, name='allusers_user'),

    path('newpost/', PostSubmission.as_view(), name="newpost"),
    path('editpost/<str:pk>', ChangePostView.as_view(), name="editpost"),
    path('deletepost/<str:pk>', delete_post, name="delete_post"),
    path('delete/success',  TemplateView.as_view(template_name='vibbo/post_delete.html'), name="post_deleted"),
    path('profile/posts', views.all_posts, name="all_posts"),
    path('allposts', views.all_users_posts, name="all_users_posts"),
    path(r'post/<str:pk>/', views.get_post_with_comments, name="post_view"),
    path('favourite/<str:pk>', views.favourite_post, name='favourite_post'),
    path('unfavourite/<str:pk>', views.unfavourite_post, name="unfav_post"),
    path('favourites', views.get_all_favourites, name="all_favourites"),

    path(r'followuser/<int:id>', views.followUser, name="follow_user"),
    path(r'unfollowuser/<int:id>', views.unfollowUser, name="unfollow_user"),
    path('home/followingsposts', views.getAllMyFollowsPosts, name="all_followings_posts"),

    path('searchposts', TemplateView.as_view(template_name='vibbo/search_posts_page.html'), name="search_posts"),
    path('foundposts/<str:search_type>/<str:search_string>', views.found_posts, name="found_posts"),
]
