from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Expense(models.Model):
    why = models.CharField(max_length=200, help_text="What is an Expense?", null=True)
    amount = models.FloatField()
    date = models.DateTimeField(default=now)
    description = models.TextField(help_text="Write your expense description.")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = [
            "-date",
        ]
        verbose_name_plural = "Expense"

    def __str__(self):
        return str(self.why)

    def get_absolute_url(self):
        return "/expense/%i/" % self.id
