from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(default=0)
    date = models.DateField(default=now)
    description = models.TextField(help_text="Write Your Income Description.")
    sources = models.CharField(max_length=200)

    def __str__(self):
        return str(self.amount)

    class Meta:
        ordering = [
            "-date",
        ]
        verbose_name_plural = "Income"


# Create your models here.
# def get_absolute_url(self):
#     """Returns the url to access a detail record for this book."""
#     return reverse('book-detail', args=[str(self.id)])
