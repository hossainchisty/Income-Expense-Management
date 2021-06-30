from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    PasswordChangeForm,
    SetPasswordForm,
    UserChangeForm,
)


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST["username"]
            password = request.POST["password1"]

            user = authenticate(request, username=username, password=password)
            # auto login
            login(request, user)
            messages.success(request, "Account Created Successfully!")

            return redirect("/")
    else:
        form = RegistrationForm()

    context = {"form": form}

    return render(request, "auth/register.html", context)


@login_required(login_url="login")
def password_change_form(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Change Successfully!")
                return redirect("/")

        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "accounts/password_change.html", {"form": form})
    else:
        return redirect("login")


@login_required(login_url="login")
def profile(request):

    return render(request, "accounts/profile.html")


@login_required(login_url="login")
def setting(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully — ")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/settings.html", {"form": form})


class ImageUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_picture.html"

    def post(self, request, *args, **kwargs):
        img = request.FILES.get("image")
        user = get_object_or_404(User, username=request.user.username)
        user.profile.image = img
        user.save()
        messages.success(request, "Image Updated Successfully")
        return redirect("profile")


"""
Custome Error pages
"""


def error_404(request, exception):
    data = {}
    return render(request, "errors/404.html", data)


# def error_500(request, exception):
#     data = {}
#     return render(request, "certman/500.html", data)
