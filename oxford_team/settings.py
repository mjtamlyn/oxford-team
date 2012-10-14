# Django settings for oxford_team project.
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import dj_database_url


DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

DEBUG = bool(os.environ.get('DEBUG', False))

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/oxford_team')}

ADMINS = (('Admin', 'marc.tamlyn@gmail.com'),)
MANAGERS = ADMINS
ADMIN_EMAILS = zip(*ADMINS)[1]
EMAIL_SUBJECT_PREFIX = '[oxford_team] '
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'marc.tamlyn@gmail.com'
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

TIME_ZONE = 'UTC'
USE_L10N = True  # Locale
USE_TZ = True

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-GB')
USE_I18N = True  # Internationalization

# Static
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'),)
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'oxford_team.urls'
SECRET_KEY = 'o$-hdw5%tq@ijxs9&r3*$y57v8b!wlfjadus(2k&a4s8qiu'
SITE_ID = 1
WSGI_APPLICATION = 'oxford_team.wsgi.application'

INSTALLED_APPS = (
    'oxford_team',

    'socialregistration',
    'socialregistration.contrib.facebook',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'socialregistration.contrib.facebook.auth.FacebookAuth',
)
LOGIN_REDIRECT_URL = '/'

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_SECRET_KEY = os.environ.get('FACEBOOK_SECRET_KEY')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
