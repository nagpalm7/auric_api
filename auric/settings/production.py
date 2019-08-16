from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*'] #['your_local_domain']  

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'auric',
        'USER': 'auricuser',
        'PASSWORD': 'Dogu123!@#',
        'HOST': 'localhost',
        'PORT': '',
    }
}
