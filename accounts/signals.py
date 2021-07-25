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
        """
        subject = "Welcome to Income Expense Manager"
        message = f"Hi there, \n\n\n Thanks {user.username} for signing up to keep in touch with your finances partner, We're so glad you are here! \n\n We can control our finances, you will know how much you spend, you have more control over money and a smaller saving problem. \n\n\n \n Cheers,\n Dev Team"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        """
        body = render_to_string("welcome_email.html", {"user": user})
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
