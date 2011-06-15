
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Abhilash Joseph C, 'abhilash@pixelcode.ca'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'votrasi',  
        'USER': 'root', 
        'PASSWORD': '', 
    }
}


TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'y7*o-x-1ovjn4yy8@mh=s&-=@ezk@ylz#4y0#yrpmv+#g-5f-y'
TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	#"django.core.context_processors.static",
	"django.contrib.messages.context_processors.messages"
)
MIDDLEWARE_CLASSES=(
	 'django.middleware.common.CommonMiddleware',
	 'django.contrib.sessions.middleware.SessionMiddleware',
	 'django.middleware.csrf.CsrfViewMiddleware',
	 'django.contrib.auth.middleware.AuthenticationMiddleware',
	 'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Votersi.urls'

TEMPLATE_DIRS = (
  os.path.join(os.path.dirname(__file__), "templates"),
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'gallery',
    'filebrowser',
)

TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True
TINYMCE_FILEBROWSER = False
