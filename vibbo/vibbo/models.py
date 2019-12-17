from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils.timezone import now
from datetime import datetime
# Create your models here.

now = datetime.now()
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    bio = models.CharField(max_length=500, blank=True)

    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    location_code = models.fields.IntegerField(blank=True, default=0)

    objects = models.Manager()
    follows = models.ManyToManyField('Profile', related_name='followed_by', blank=True)


@receiver(post_save, sender=User)
def profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, blank=True)
    body = models.CharField(max_length=1023, blank=True)

    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    location_code = models.fields.IntegerField(max_length=30, blank=True)

    date = models.DateField(default=now)
    time = models.TimeField(default=now)

    objects = models.Manager()

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    post_reference = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment_body = models.CharField(max_length=1023, blank=True)

    date = models.TimeField(default=now)

    objects = models.Manager()

    class Meta:
        ordering = ['-date']


class Favourites(models.Model):
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE)
    post_ref = models.ForeignKey(Post, on_delete=models.CASCADE)

    objects = models.Manager()

