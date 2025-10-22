# billing_api/settings.py
from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY','secret-key')
DEBUG = os.getenv('DEBUG','True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
  'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
  'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
  'rest_framework','django_filters',
  'users',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "billing_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "billing_api.wsgi.application"

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES':(
    'rest_framework_simplejwt.authentication.JWTAuthentication',
  ),
  'DEFAULT_PERMISSION_CLASSES':(
    'rest_framework.permissions.IsAuthenticated',
  ),
  'DEFAULT_FILTER_BACKENDS':(
    'django_filters.rest_framework.DjangoFilterBackend',
    'rest_framework.filters.SearchFilter',
    'rest_framework.filters.OrderingFilter',
  ),
  'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
  'PAGE_SIZE':10
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'billingdb',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
  'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

STATIC_URL='static/'