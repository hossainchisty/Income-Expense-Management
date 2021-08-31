"""
Title: Income Expense Manager
Author: Hossain Chisty
Description: Income expense manager is easiest and user friendly application to control your finance.
Contact: hossain.chisty11@gmail.com
"""
import os
import django_heroku
import dj_database_url
from pathlib import Path
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( cloud_name="hossainchisty", 
                    api_key="958916513788356", 
                    api_secret="2BaQjUoM5jHa3K6VVpbaSs_icBQ" )

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "_41ckb9(nmeg6*^tg5&jjf8e9s@(yfwl5dxk)1afiy0d720y!4"

DEBUG = True

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

if DEBUG == False:
    SECURE_SSL_REDIRECT = True

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
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
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },
}
"""
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
"""

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Cache middleware configuration
    # "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
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
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Database caching
# https://docs.djangoproject.com/en/3.2/topics/cache/

# The cache timeout, in seconds
# CACHE_MIDDLEWARE_SECONDS = 20

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.db.DatabaseCache",
#         "LOCATION": "income_expenses_manager_caches",
#     }
# }

# python manage.py createachetable
# Filesystem caching

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
#         "LOCATION": "G:\Income and expenses\cache",
#     }
# }


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



STATIC_URL = "/static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# sTATIC FILES Configuration
STATICFILES_DIRS = ["static"]
# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# SMTP Configuration
EMAIL_HOST = "smtp.zoho.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = "hossain.chisty@zohomail.com"
DEFAULT_EMAIL_FROM = '<noreply@hossain.chisty@zohomail.com>'
EMAIL_HOST_PASSWORD = "#2#3B399TiU@aBC"
EMAIL_USE_SSL = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

CRISPY_TEMPLATE_PACK = "bootstrap4"

django_heroku.settings(locals(), test_runner=False)