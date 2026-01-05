from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#signal is post_save, we have a sender and reciever
#reciever is the function, itself which recieves information on the instance, created, sender
#reciever than saves, updates, creates with the instance data
#signals important so user can create and save pfp without going through admin access/page