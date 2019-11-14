Monolith example
=======

This code is an evolution from the Monolith. It is a Django application (https://www.djangoproject.com/) that creates a website for microblogging. It connects to both the users backend and the thoughts backend.

**THIS IS AN EXAMPLE WEBSITE**

Set it up
------

Use docker-compose to build the service

    $ docker-compose build

Configure the `environment.env` file to point to the users and thoughts backend. Use the
IP on your local machine.


Up the service

    $ docker-compose up


Test and login
------

There are two users created in the system, `bruce` and `stephen`, their password are "password".

You can log in as any of them, add more "throughs", and search for all the thoughts in the system. No need to be logged to search.


Dependencies
------

MyThoughts uses Django as a web framework, Bootstrap for the styling and bcrypt for checking the passwords. Please note that the way of handling authentication is not safe and shouldn't be used in a production website.
