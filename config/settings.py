"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 2.2.5.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import json
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json

with open(secret_file, 'r') as f: # open as secret.json
    secrets = json.loads(f.read())
    
def get_secret(setting, secrets=secrets): # 예외 처리
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

EMAIL_SECRET_KEY = get_secret("SECRET_KEY")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#*s_so_hno1sj=3!6u4#zy_=q0ppng4oszaf@lo5u2gwg+$6d7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "debug_toolbar",
    'Login',
    'emotion_calendar',
    'diary',
    'widget_tweaks',
    'bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'channels',
]

SITE_ID = 1

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 미들웨어 추가
    'Login.middleware.ProfileSetupMiddleware',
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
ASGI_APPLICATION = 'config.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('localhost', 6379)]
        }
    }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'Login.validators.CustomPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR , 'static']
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/uploads/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "Login.User"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# url 설정
ACCOUNT_SIGNUP_REDIRECT_URL= "profile-set" # 회원가입을 하면 profile-set 이동
LOGIN_REDIRECT_URL="cal:calendar" # 로그인을 하면 calendar로 이동
ACCOUN_LOGOUT_REDIRECT_URL= "account_login" # 로그아웃 하면 로그인으로
LOGIN_URL = 'account_login' # 로그인이 안 된다면 로그인 페이지로 이동
ACCOUNT_LOGOUT_ON_GET=True # 바로 로그아웃 (기본 값은 False)
ACCOUNT_AUTHENTICATION_METHOD= "email"  # email로 유저 로그인
ACCOUNT_EMAIL_REQUIRED = True  # 회원가입시 email 필수
ACCOUNT_USERNAME_REQUIRED = False # 회원가입시 username 선택
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
ACCOUNT_EMAIL_VARIFICATION = "optional" # 인증 하지 않아도 로그인 가능
ACCOUNT_SESSION_REMEMBER= True # 유저 기억
ACCOUNT_CONFIRM_EMAIL_ON_GET = True # 이메일 인증링크로 들어가면 바로인증 되게함


# 로그인시 이메일 인증이 되었을때 /되지 않았을때 인증 URL 설정
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL= "account_email_confirmation_done"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL= "account_email_confirmation_done"
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

# Email settings 이메일 인증을 위함
# gmail
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rkdalstj4505@gmail.com'
EMAIL_HOST_PASSWORD= EMAIL_SECRET_KEY


# Django-debug-toolbar settings
INTERNAL_IPS = ['127.0.0.1']
