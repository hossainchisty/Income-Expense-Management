from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import RegistrationForm, ProfileForm
from .decorators import unauthenticated_user
from django.contrib.auth.forms import (
    PasswordChangeForm,
    # A form for allowing a user to change their password.
    SetPasswordForm,
    # A form that lets a user change their password without entering the old password.
    UserChangeForm,
    # A form used in the admin interface to change a user’s information and permissions.
    PasswordResetForm,
    # A form for generating and emailing a one-time use link to reset a user’s password.
)


@unauthenticated_user
def register(request):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
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
    """
    A form for allowing a user to change their password.
    """
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


@login_required(login_url="login")
def deactivateUser(request):
    user = request.user
    user.is_active = False
    user.is_staff = False
    user.is_superuser = False
    user.save()
    messages.success(request, "Profile successfully disabled.")
    return redirect("/")


@login_required(login_url="login")
def deactivatePage(request):
    return render(request, "accounts/deactivate.html")


class ImageUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile_picture.html"

    def post(self, request, *args, **kwargs):
        img = request.FILES.get("image")
        user = get_object_or_404(User, username=request.user.username)
        user.profile.image = img
        user.save()
        messages.success(request, "Image Updated Successfully")
        return redirect("profile")


def page_not_found_error(request, exception):
    return render(
        request,
        "errors/404.html",
        context={"error": "Access error: page does not exist"},
        status=404,
    )


def page_error(request):
    """
    Processing for any otherwise uncaught exceptions (those that will generate HTTP 500 responses).
    """
    return render(
        request,
        "errors/500.html",
        context={"error": "Access error: server error"},
        status=500,
    )
