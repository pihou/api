# -*- coding: utf-8 -*-
from getenv import env

import dotenv
import dj_database_url
import os
import sys

dotenv.read_dotenv()

DEBUG = env('DEBUG', False)
SECRET_KEY = '-p7542&i63aar3)8ej)@*m_ail5#y&ga)p!$%rqkeyii66_o=n'
ROOT_URLCONF = 'api.urls'
WSGI_APPLICATION = 'api.wsgi.application'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_HOSTS = ['*']
APPEND_SLASH = True
LANGUAGE_CODE = 'zh-Hans'
USE_L10N = False
USE_I18N = False
USE_TZ = env('USE_TZ', True)
TIME_ZONE = env('TIME_ZONE', 'Asia/Shanghai')

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',
    'app',
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000000/second',
        'user': '1000000/second'
    },
    'EXCEPTION_HANDLER': 'api.rest_custom.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 12 
}

MIDDLEWARE = [
]

#DATABASES = {
#    'default': dict(
#        dj_database_url.parse(env("DATABASE_URI", "mysql://api:api@mysql:3306/api")),
#        ATOMIC_REQUESTS=True,
#        CONN_MAX_AGE=3600*6,
#        OPTIONS={
#            'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci,sql_mode=STRICT_TRANS_TABLES'
#        }
#    ),
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        "CONN_MAX_AGA":3600,
    }
}
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        "CONN_MAX_AGA":3600,
    }

REDIS_URL = env("REDIS_URL", "redis://redis:6379")
REDIS_LOGIN = REDIS_URL + "/0"
REDIS_MISC  = REDIS_URL + "/1"

#ADMINS = (('Monkey', 'bufan@szxintom.com'))
EMAIL_HOST='smtp.exmail.qq.com'
EMAIL_PORT=465
EMAIL_HOST_USER='tech@szxintom.com'
EMAIL_HOST_PASSWORD='TE@2018aaa'
EMAIL_USE_SSL = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] [%(levelname)s] %(funcName)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'error': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'access': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

