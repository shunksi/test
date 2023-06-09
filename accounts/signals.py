from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User
'''
With this signal when user register make a profile for user automatically

'''

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
