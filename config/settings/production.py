# 운영, 배포 환경

import os
from .base import *

# 로컬, 작업 환경

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['13.125.157.195']

DJANGO_APPS += [

]
PROJECT_APPS += [

]
THIRD_PARTY_APPS += [
    
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATICFILES_DIRS =[]
STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')