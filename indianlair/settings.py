"""
Django settings for indianlair project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from machina import get_apps as get_machina_apps

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!o(lmxt25$fbl+!hp3bchp)sy-as813j#dqyaec&7=3-758z_k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Machine related apps:
    'mptt',
    'haystack',
    'widget_tweaks',
] + get_machina_apps()

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
]

ROOT_URLCONF = 'indianlair.urls'

from machina import MACHINA_MAIN_TEMPLATE_DIR
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), 
            MACHINA_MAIN_TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'machina.core.context_processors.metadata',
            ],
        },
    },
]
# TEMPLATE_CONTEXT_PROCESSORS = (    )

WSGI_APPLICATION = 'indianlair.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'indianlair.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
from machina import MACHINA_MAIN_STATIC_DIR

STATIC_URL = '/static/'

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        MACHINA_MAIN_STATIC_DIR,
    )


CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments':{
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION':'/tmp',
    }
}

HAYSTACK_CONNECTIONS = {
  'default': {
    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    # For using Whoosh or Solr, but currently I don't know if I've to import
    # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
    # 'PATH': os.path.join(PROJECT_PATH, 'whoosh_index'),
  },
}

AUTH_PASSWORD_VALIDATORS = []
# Removed password checking for simple password from admin (and maybe other places)
# Change it during production
# http://stackoverflow.com/questions/35032159/how-to-set-simple-password-in-django-1-9#comment57789923_35032185