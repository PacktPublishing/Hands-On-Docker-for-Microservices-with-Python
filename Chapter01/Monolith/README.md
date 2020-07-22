Monolith example
=======

This code is our example of Monolith. It is a Django application (https://www.djangoproject.com/) that creates a website for microblogging.

**THIS IS AN EXAMPLE WEBSITE**

Set it up
------

Create a virtual environment and install the requirements

    $ python3 -m venv ./venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt


Get the local database ready and load some initial data for testing

    $ cd mythoughts/
    $ python manage.py migrate
    ...
    $ python manage.py loaddata thoughts/fixtures/thoughts.json thoughts/fixtures/users.json
    Installed 7 object(s) from 2 fixture(s)

Start the development server

    $ python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    ...
    Django version 2.2.1, using settings 'mythoughts.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Check the service at http://127.0.0.1:8000/


Test and login
------

There are two users created in the system, `bruce` and `stephen`, their password are "password".

You can log in as any of them, add more "throughs", and search for all the thoughts in the system. No need to be logged to search.


Dependencies
------

MyThoughts uses Django as a web framework, Bootstrap for the styling and bcrypt for checking the passwords. Please note that the way of handling authentication is not safe and shouldn't be used in a production website.
