import os
from pathlib import Path
from celery.schedules import crontab
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", default=0)


ALLOWED_HOSTS = ['*']
# CSRF_TRUSTED_ORIGINS = ["https://8d55-94-143-198-2.eu.ngrok.io"]


# Application definition

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'phonenumber_field',
    'drf_yasg',

    "users",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "artwaga"),
        "USER": os.environ.get("SQL_USER", "postgres"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "postgres"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

MEDIA_URL = "/data/"
MEDIA_ROOT = "data"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

# REST Files

REST_FRAMEWORK = {
        'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.IsAdminUser', ),
}

SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': timedelta(days=os.environ.get('REFRESH_TOKEN_LIFETIME', 7)),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=os.environ.get('ACCESS_TOKEN_LIFETIME', 1)),
    'ROTATE_REFRESH_TOKENS': True,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

CORS_ORIGIN_ALLOW_ALL = True

SMS_NIKITA_LOGIN = os.environ.get('SMS_NIKITA_LOGIN')
SMS_NIKITA_PASSWORD = os.environ.get('SMS_NIKITA_PASSWORD')
SMS_NIKITA_SENDER_NAME = os.environ.get('SMS_NIKITA_SENDER_NAME')

PAYBOX_URL = 'https://api.paybox.money/payment.php'
PAYBOX_PROJECT_ID = os.environ.get('PAYBOX_PROJECT_ID')
PAYBOX_SECRET_KEY = os.environ.get('PAYBOX_SECRET_KEY')

PAYBOX_SALT = os.environ.get('PAYBOX_SALT')
PAYBOX_SUCCESS_URL_METHOD = 'GET'
PAYBOX_CURRENCY = 'KGS'
PAYBOX_LANGUAGE = 'ru'
PAYBOX_SUCCESS_URL = os.environ.get('PAYBOX_SUCCESS_URL')
PAYBOX_RESULT_URL = os.environ.get('PAYBOX_RESULT_URL')
PG_SITE_URL = os.environ.get('PG_SITE_URL')


# Redis and Celery

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379")

CELERY_BEAT_SCHEDULE = {
    "sample_task": {
        "task": "sample_task",
        "schedule": crontab(minute="*/1"),
    },
}
