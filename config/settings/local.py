from .base import *

SECRET_KEY = ('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'staticfiles')

