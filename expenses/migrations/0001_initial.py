# Generated by Django 3.2.4 on 2021-09-17 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('why', models.CharField(help_text='What is an Expense?', max_length=200, null=True)),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(help_text='Write your expense description.')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Expense',
                'ordering': ['-date'],
            },
        ),
    ]
