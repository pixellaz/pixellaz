# Django settings for pixellaz project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Duy Nguyen', 'coldzero1120@gmail.com'),
)

MANAGERS = ADMINS

import os
from local_settings import *

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static')
MEDIA_URL = '/static/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.request',
    'django.core.context_processors.media',
    'pixelcms.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
	#'pixelcms.apps.auth.UserAuthBackend',
)

SESSION_ENGINE = 'mongoengine.django.sessions'

ROOT_URLCONF = 'urls'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.sessions',
	'pixelcms',
	'pixeltheme',
)

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/admin/'

TEST_RUNNER = 'testrunner.run_tests'

PIXELCMS_PIXELCMS_MARKUP_LANGUAGE = 'markdown'
PIXELCMS_THEME = 'pixeltheme'