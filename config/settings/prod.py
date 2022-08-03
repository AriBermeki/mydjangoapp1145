from .base import * 

from decouple import config
import django_on_heroku

SECRET_KEY = config('SECRET_KEY ')


DEBUG = False
ALLOWED_HOSTS = ['django-aws-heroku-settings.heroku.com']


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID ')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL= 'publice-read'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl':'max-age=86400'}
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {'Access-Control-Allow-Origin':'*'}
DEFAULT_FIELD_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media'


# Heroku Settings



DEBUG_PROPAGATE_EXEPTIONS = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose':{
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler'
        },
    },
    'loggers':{
        'MYAPP':{
            'handlers':['console'],
            'level':'DEBUG'
        },
    },

}

django_on_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']

#'django-insecure-6$e@fr_sg@e@$y@^uyetl%*qoj^d@hs+-d$spd8$4yj)0)$b@)'
#https://django-aws-heroku-settings.herokuapp.com/ | https://git.heroku.com/django-aws-heroku-settings.git