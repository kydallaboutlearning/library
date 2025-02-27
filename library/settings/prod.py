"""Setting up the setting for production"""
# importing requirements
from .base import *




DEBUG = False

ALLOWED_HOSTS = [".pythonanywhere.com",'127.0.0:8000',]


INSTALLED_APPS += ["whitenoise.runserver_nostatic", 
                    ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"] 
STATIC_ROOT = BASE_DIR / "staticfiles" 
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" 