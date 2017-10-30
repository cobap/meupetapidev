import dj_database_url

from meupetapi.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
	'localhost',
	u'http://127.0.0.1',
	'.herokuapp.com'
]

SECRET_KEY = get_env_variable('SECRET_KEY')

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
#heroku pg:reset DATABASE_URL
#heroku run python manage.py makemigrations
#heroku run python manage.py migrate
#- apaga tudo e reseta banco do zero - então basta rodar migration para recriar.

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
