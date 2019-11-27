# accounts/urls.py
from django.urls import path, re_path
from .views import ChangeProfileView, DisplayDetailView, PostSubmission, PostView, ChangePostView, delete_post
from . import views
from .models import Post
from django.views.generic import TemplateView


urlpatterns = [
    path(r'profile/<int:pk>/', DisplayDetailView.as_view(), name='profile'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', views.SignUp.as_view(), name='home'),
    path('home/allusers', views.allUsers, name='allusers'),
    path('home/allusers/<str:pk>/', views.allUsers, name='allusers_user'),
    path('change/', ChangeProfileView.as_view(), name='change'),
    path('newpost/', PostSubmission.as_view(), name="newpost"),
    path('editpost/<str:pk>', ChangePostView.as_view(), name="editpost"),
    path('deletepost/<str:pk>', delete_post, name="delete_post"),
    path('delete/success',  TemplateView.as_view(template_name='vibbo/post_delete.html'), name="post_deleted"),
    path('profile/posts', views.all_posts, name="all_posts"),
    path(r'post/<str:pk>/', PostView.as_view(model=Post), name="post_view")
]