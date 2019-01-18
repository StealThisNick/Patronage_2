========
Machine
========

Machine is a Testing task from Intive, for patronage 2019 Machine Learning & Big Data.

1. Machine have two view, first: index with two buttons, secound: detailed table
2. First button: redirect to detailed view, secound button: load salary.csv file to model
3. Detailed view estimate salary over years and add it to the table


Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "machine" to your INSTALLED_APPS and also add cripsy template pack setting like this::

    INSTALLED_APPS = [
        ...
        'machine',
    ]

    CRISPY_TEMPLATE_PACK = 'bootstrap4'

2. Include the polls URLconf in your project urls.py like this::

    path('machine/', include('machine.urls')),

3. Install django-crispy-forms::

    pip install django-crispy-forms

4. Run `python manage.py migrate` to create the machine models.


5. Visit http://127.0.0.1:8000/machine/ to participate in the machine.