import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '$ew^+y)(zn4^7ktmzix44pp0ppunk%_dsrd66zqg05ai5u16o@'

DEBUG = TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

CUSTOM_APPS = (
	'Bomber',
    'Command'
)

INSTALLED_APPS += CUSTOM_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Bomb.urls'

WSGI_APPLICATION = 'Bomb.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = USE_L10N = USE_TZ = True

STATIC_URL = '/static/'
COMMAND_FILE = 'commands'

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'bower_components'),
)