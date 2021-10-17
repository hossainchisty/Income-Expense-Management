"""
Title: Income Expense Manager
Description: Income expense manager is easiest and user friendly application to control your finance.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty
"""
import os
import django_heroku
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Configure cloudinary
cloudinary.config(cloud_name="hossainchisty", api_key="958916513788356", api_secret="2BaQjUoM5jHa3K6VVpbaSs_icBQ")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

if DEBUG is False:
    SECURE_SSL_REDIRECT = True
else:
    SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ["127.0.0.1:8000", "django-income-expense-manager.herokuapp.com"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local apps
    "income.apps.IncomeConfig",
    "expenses.apps.ExpensesConfig",
    "accounts.apps.AccountsConfig",
    # third party apps
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    "crispy_forms",
    "django_countries",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "cloudinary",
    # providers to enable for social login:
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",

]
# production
SITE_ID = 2

# local
# SITE_ID = 3

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },
}

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Project.wsgi.application"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_L10N = True

USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Static files configuration
STATICFILES_DIRS = ["static"]
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Crispy Form Pack - Bootstrap 4
CRISPY_TEMPLATE_PACK = "bootstrap4"

# SMTP Configuration
EMAIL_HOST = "smtp.zoho.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "hossain.chisty@zohomail.com"
DEFAULT_EMAIL_FROM = '<noreply@hossain.chisty@zohomail.com>'
EMAIL_HOST_PASSWORD = "#2#3B399TiU@aBC"
EMAIL_USE_SSL = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'


# Activate Django-Heroku.
django_heroku.settings(locals(), test_runner=False)
