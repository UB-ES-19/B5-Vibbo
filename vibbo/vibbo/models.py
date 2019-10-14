from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    occupation = models.CharField(max_length=500,blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    objects=models.Manager()

@receiver(post_save, sender=User)
def profile_for_new_user(sender, instance , created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()
