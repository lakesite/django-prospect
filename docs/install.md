# install #

1. Install django-prospect into your python environment

    $ virtualenv .env
    $ source .env/bin/activate
    $ (.env) python setup.py install

    Alternatively:

    $ (.env) pip install -e git+https://github.com/lakesite/django-prospect.git#egg=django-prospect

2. Add django-prospect to your INSTALLED_APPS in your settings.py:

# settings.py

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # ...
    'django-prospect'
)

3. Run `migrate prospect` to create the prospect tables.

    (.env) $ python manage.py migrate prospect
    Operations to perform:
      Apply all migrations: prospect
    Running migrations:
      Applying prospect.0001_initial... OK
    (.env) $
