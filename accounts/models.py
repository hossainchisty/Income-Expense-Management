from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles", default="profiles/default.png")

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.user.username
