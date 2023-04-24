Thoughts Backend example
=======

This code is our example of Thoughts Engine. It is a Flask application (https://www.djangoproject.com/) that creates a RESTful backend to store microblogging posts.

**THIS IS AN EXAMPLE WEBSITE**

Set it up
------

Create a virtual environment and install the requirements

    $ python3 -m venv ./venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt


Get the local database ready

    $ python init_db.py

Start the development server (in Unix)

    $ FLASK_APP=wsgi.py flask run
    * Serving Flask app "wsgi.py"
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit

Check the service at http://127.0.0.1:5000/


Start the development server (in Windows Powershell)

    $ set FLASK_APP=wsgi.py
    $ FLASK_APP=wsgi.py flask run
    * Serving Flask app "wsgi.py"
    * Environment: production
      WARNING: Do not use the development server in a production environment.
      Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)    
    

Tests
------

Run the unit tests with

    $ pytest


Dependencies
------

ThoughtsBackend uses Flask as a web framework, Flask RESTplus for creating the interface, and SQLAlchemy to handle the database models. It uses a SQLlite database for local development.
