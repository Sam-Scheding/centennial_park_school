"""
Django settings for centennial_park_school project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import datetime
from datetime import time
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z5n2jndq2cm#bfqzig1e45+8q&)aw*ndk(h@j$ge0mz1=v!pc5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'webapp-384830.pythonanywhere.com', 'www.centennialparkschool.nsw.edu.au', 'www.centennialparkschool.nsw.edu.au']


# Application definition

INSTALLED_APPS = [
    'apps.main',
    'apps.contact',
    'apps.staff',
    'apps.console',
    'apps.behaviour',
    'apps.api',
    'apps.downloads',
    'apps.blog',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'centennial_park_school.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'main/templates/',
            'gallery/templates/',
            'contact/templates/',
            'console/templates/',
            'staff/templates/',
            'behaviour/templates',
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'centennial_park_school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'cps_external', 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main', 'static'),
    os.path.join(BASE_DIR, 'staff', 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

CONTACT_EMAILS = [
    'sam.scheding1@det.nsw.edu.au',
    'samscheding@gmail.com',
    'centennial-s.school@det.nsw.edu.au',
]

FILE_CHARSET = "utf-8"

EMAIL_HOST = "in-v3.mailjet.com"
EMAIL_HOST_USER = "4973c25f516c04a4434a0b2c3375dca0"
EMAIL_HOST_PASSWORD = 'c863b3b59c557cfade23c5d259807a1b'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

WEEK_CHOICES = []
for r in range(1, 13):
    WEEK_CHOICES.append((r, r))

TERM_CHOICES = [(1,1),(2,2),(3,3),(4,4)]

SCHOOL_YEARS = [(7,7), (8,8), (9,9), (10,10), (11,11), (12,12)]
CURRENT_TERM = 4  # TODO: Figure a better way around this than hardcoding
CURRENT_YEAR = datetime.datetime.now().year

SCHOOL_TIMES = [
        (time(9, 00, 00), time(9, 00, 00)), (time(9, 30, 00), time(9, 30, 00)),
        (time(10, 00, 00), time(10, 00, 00)), (time(10, 30, 00), time(10, 30, 00)),
        (time(11, 00, 00), time(11, 00, 00)), (time(11, 30, 00), time(11, 30, 00)),
        (time(12, 00, 00), time(12, 00, 00)), (time(12, 30, 00), time(12, 30, 00)),
        (time(13, 00, 00), time(13, 00, 00)), (time(13, 30, 00), time(13, 30, 00)),
        (time(14, 00, 00), time(14, 00, 00)), (time(14, 30, 00), time(14, 30, 00)),
    ]

ATTENDANCE_OPTIONS = [
        # (0, '------'),
        (1, 'Attended'),
        (2, 'Absent (Explained)'),
        (3, 'Absent (Unexplained'),
        (4, 'Integrating'),
        (5, 'Suspended'),
        (6, 'Public Holiday'),
    ]

BT_YEAR_CHOICES = [(r, r) for r in range(CURRENT_YEAR, CURRENT_YEAR + 5)]

WEEKDAYS = [('Monday', 'Monday'),('Tuesday','Tuesday'),('Wendesday','Wendesday'),('Thursday','Thursday'),('Friday','Friday')]
YEAR_CHOICES = []  # Change to list comprehension and replace 2010 with datetime.datetime.now().year - 10
for r in range(2010, (CURRENT_YEAR + 1)):
    YEAR_CHOICES.append((r, r))

TERMS = [('Term 1', 'Term 1'), ('Term 2', 'Term 2'), ('Term 3', 'Term 3'), ('Term 4', 'Term 4')]
CLASSES = [('', ''), ('C1', 'C1'), ('C2', 'C2'), ('C3','C3'), ('C4','C4'), ('C5','C5'), ('C6','C6')]
WIO_TYPE = [('','--------'), ('System', 'System'), ('Instant', 'Instant')]
STAFF_TITLES = [('Executive', 'Executive'), ('Teaching', 'Teaching'), ('Non-Teaching', 'Non-Teaching'), ('Other', 'Other')]

LOGIN_REDIRECT_URL = '/console'
LOGOUT_REDIRECT_URL = '/'
