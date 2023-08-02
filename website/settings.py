"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages
import vercel

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7u@$%$bh_64)&#iic9$2h)%)s@fh%!o_74t^69r7$3h^klg)*q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', vercel.get_host()]


# Application definition

INSTALLED_APPS = [
    'business.apps.BusinessConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
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

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / "templates")],
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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql',
      'NAME':'Contact',
      'USER':'postgres',
      'PASSWORD':'Zaini@786',
      'HOST':'localhost',
      'PORT':'5432',
   }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
############################### Added manually ###################################

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# MESSAGE_TAGS = {messages.INFO: "",50: "critical",}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


##################################### Email Backend #########################################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com' # gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "zainiomp@gmail.com"
EMAIL_HOST_PASSWORD = "uqwfrodkqbizxvdb"



############################################ AWS ########################################
import boto3
from storages.backends.s3boto3 import S3Boto3Storage

DEFAULT_FILE_STORAGE = 'website.storage_backends.MediaStorage'

STATICFILES_STORAGE = 'website.storage_backends.StaticStorage'

AWS_STORAGE_BUCKET_NAME = 'omp-786'

AWS_S3_REGION_NAME = 'ap-south-1'

AWS_ACCESS_KEY_ID = 'AKIASJAKYGE7EEMYAAM3'

AWS_SECRET_ACCESS_KEY = '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'