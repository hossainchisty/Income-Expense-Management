from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
