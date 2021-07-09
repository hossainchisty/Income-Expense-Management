import uuid
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class Profile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles", default="profiles/default.png")
    bio = models.TextField(null=True, blank=True)
    phone_number = RegexValidator(
        regex=r"^\+(?:[0-9]●?){6,14}[0-9]$",
        message=_(
            "Enter a valid international mobile phone number starting with +(country code)"
        ),
    )
    city = models.CharField(
        verbose_name=_("City"), max_length=400, null=True, blank=True
    )
    country = CountryField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.user.username
