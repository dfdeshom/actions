# actions

The goal of the application is to store/manage actions. A user should
be able to create, change, and delete actions. Actions can be assigned
to any user. Actions should have at least a title and a description,
and they should be capable of being displayed as a group in some
fashion relative to the current month.

## Installation
Instal dependencies:
$ pip install -r requirements.py

Migrate the database:
    
    $ python manage.py migrate

For a local environment, run

    $ python manage.py runserver

Navigate to  http://127.0.0.1:8000/actions` to see actions.


