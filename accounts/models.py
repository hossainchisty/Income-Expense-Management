from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """Profile model for storing user information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('profile-photo')
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\+?880?\d{9,11}$', message="Phone number must be entered in the format: '+8801234233566'. Up to 11 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField(
        verbose_name=_("City"), max_length=400, null=True, blank=True
    )
    country = CountryField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.user.username
