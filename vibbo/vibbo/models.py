from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    bio = models.CharField(max_length=500, blank=True)

    street = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    location_code = models.fields.IntegerField(blank=True, default=0)

    objects = models.Manager()


@receiver(post_save, sender=User)
def profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255, blank=True)
    body = models.CharField(max_length=1023, blank=True)

    date = models.DateField()

    objects = models.Manager()

    class Meta:
        ordering = ['date']


@receiver(post_save, sender=User)
def new_post_for_user(sender, instance, created, **kwargs):
    if created:
        Post.objects.create(user=instance).save()

