# development #

Extending and developing prospect is best done through the included example
django application.  

## setup ##

First create a python3 virtualenv and then activate it under two terminals:

        $ virtualenv -p python3 .env
        $ source .env/bin/activate

In one terminal you'll setup the example application and will be using the
prospect app through this project:

        (.env) example_application$ pip install -r requirements.txt
        (.env) example_application$ cd mysite
        (.env) example_application/mysite$ python manage.py migrate
        (.env) example_application/mysite$ python manage.py createsuperuser
        (.env) example_application/mysite$ python manage.py runserver

The other terminal will periodically re-install changes you've made to the app
under site-packages.

        (.env) django-prospect$ python setup.py install

## changes ##

If you change the models.py and need to make migrations, do the following,
assuming python 3.6 and django_prospect-0.1;

        rm -rf .env/lib/python3.6/site-packages/django_prospect-0.1-py3.6.egg/migrations
        (.env) django-prospect$ python setup.py sdist
        (.env) django-prospect/example_application$ rm db.sqlite3
        (.env) django-prospect/example_application$ python manage.py makemigrations prospect
        (.env) django-prospect/example_application$ python manage.py migrate
        (.env) django-prospect$ cp .env/lib/python3.6/site-packages/django_prospect-0.1-py3.6.egg/migrations/* ./migrations/

This seems a bit convoluted, if you have a better workflow, I'd love to know.

## using ##

        (.env) $ python manage.py createsuperuser
        (.env) $ python manage.py runserver

The default Django system and prospect app is accessible at:

    http://localhost:8000/admin/
