from django.conf import settings
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Profile


@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=instance)

        subject = "Welcome to Income Expense Manager"
        message = f"Hi there, \n\n\n Thanks {user.username} for signing up to keep in touch with your finances partner, We're so glad you are here! \n\n We can control our finances, you will know how much you spend, you have more control over money and a smaller saving problem. \n\n\n \n Cheers,\n Dev Team"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    else:
        instance.profile.save()
