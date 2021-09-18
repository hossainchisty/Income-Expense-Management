from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

# Email Configure imports
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=instance)
        body = render_to_string("welcome_email.html", {"user": user, "profile": profile})
        mail = EmailMessage(
            subject="Welcome to Income Expense Manager🎉",
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        mail.content_subtype = "HTML"
        mail.send()

    else:
        instance.profile.save()
