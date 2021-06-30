from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from income.models import Income


class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.FloatField(default=0)
    date = models.DateField(default=now)
    description = models.TextField(help_text="Write your expense description.")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = [
            "-date",
        ]
        verbose_name_plural = "Expense"

    def __str__(self):
        return self.name
