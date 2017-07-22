INSTALLED_APPS = (
    'qsstats',
    'django.contrib.auth',
    'django.contrib.contenttypes'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'qsstats_test',
        'USER': 'postgres',
        'PASSWORD': '',
    }
}

SECRET_KEY = 'foo'
