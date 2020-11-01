from .base import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'company-analysis.net']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'company_analysis',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': ''
    }
}

STATIC_ROOT = '/usr/share/nginx/html/static'

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY')
AWS_SES_SECRET_ACCESS_KEY_ID = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')

#ロギング

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     #ロガーの設定
#     'loggers':{
#         #djangoが利用するロガー
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#         },
#         #configアプリケーションが利用するロガー
#         'config':{
#             'handlers': ['file'],
#             'level': 'INFO',
#         },
#     },

#     #ハンドラの設定
#     'handlers':{
#         'file':{
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join(BASE_DIR,'logs/django.log'),
#             'formatter': 'prod',
#             'when': 'D',
#             'interval': 1,
#             'backupCount': 7,
#         },
#     },

#     #フォーマッタの設定
#     'formatters':{
#         'prod':{
#             'format':'\t'.join([
#                 '%(asctime)s',
#                 '[%(levelname)s]',
#                 '%(pathname)s(Line:%(lineno)d)',
#                 '%(message)s'
#             ])
#         },
#     }
# }

# # heroku用
# import dj_database_url
# DATABASES['default'] = dj_database_url.config()

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ALLOWED_HOSTS = ['*']

# STATIC_ROOT = 'staticfiles'

# DEBUG = False

# try:
#     from .local_settings import *
# except ImportError:
#     pass