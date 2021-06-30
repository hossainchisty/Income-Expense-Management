from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Registration and Login
    path("sign-up/", views.register, name="register"),
    path(
        "sign-in/",
        auth_views.LoginView.as_view(template_name="auth/login.html"),
        name="login",
    ),
    path(
        "sign-out/",
        auth_views.LogoutView.as_view(template_name="auth/logout.html"),
        name="logout",
    ),
    # Password Reset with email
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="auth/forgot-password.html"),
        name="password_reset",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
    path("profile/", views.profile, name="profile"),
    path("settings/profile/", views.setting, name="setting"),
    path("profile/edit/", ImageUpdateView.as_view(), name="update_image"),
    # password change with old password
    path("password/change/", views.password_change_form, name="password-change"),
]
