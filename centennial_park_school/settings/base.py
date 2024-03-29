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
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z5n2jndq2cm#bfqzig1e45+8q&)aw*ndk(h@j$ge0mz1=v!pc5'

ALLOWED_HOSTS = []


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


REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # 'main/templates/',
            # 'gallery/templates/',
            # 'contact/templates/',
            # 'console/templates/',
            # 'staff/templates/',
            # 'behaviour/templates',
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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps', 'main', 'static'),
    os.path.join(BASE_DIR, 'apps', 'staff', 'static'),
]

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


ENROLMENT_CAPACITY = 42
WEEK_CHOICES = []
for r in range(1, 13):
    WEEK_CHOICES.append((r, r))

TERM_CHOICES = [(1,1),(2,2),(3,3),(4,4)]

SCHOOL_YEARS = [(7,7), (8,8), (9,9), (10,10), (11,11), (12,12)]
CURRENT_TERM = 4  # TODO: Figure a better way around this than hardcoding
CURRENT_YEAR = datetime.datetime.now().year

SCHOOL_TIMES = [
        (time(9, 00, 00), "9:00 am"), (time(9, 30, 00), "9:30 am"),
        (time(10, 00, 00), "10:00 am"), (time(10, 30, 00), "10:30 am"),
        (time(11, 00, 00), "11:00 am"), (time(11, 30, 00), "11:30 am"),
        (time(12, 00, 00), "12:00 pm"), (time(12, 30, 00),"12:30 pm"),
        (time(13, 00, 00), "1:00 pm"), (time(13, 30, 00), "1:30 pm"),
        (time(14, 00, 00), "2:00 pm"), (time(14, 30, 00), "2:30 pm"),
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
