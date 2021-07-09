from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Note: it just works for username
        # help_texts = {
        #     "username": None,
        #     "email": None,
        #     "password1": None,
        #     "password2": None,
        # }


class ProfileForm(UserChangeForm):
    # A form used in the admin interface to change a user’s information and permissions.
    password = None
    # date_joined = forms.DateTimeField(disabled=True)
    # last_login = forms.DateTimeField(disabled=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]
        labels = {
            "email": "Email",
            "username": "Username",
        }
        help_texts = {
            "username": None,
        }


# class ExtraProfile(ProfileForm):
#     bio = forms.CharField(widget=forms.Textarea)

#     class Meta(ProfileForm.Meta):
#         fields = ProfileForm.Meta.fields + [
#             "bio",
#         ]
