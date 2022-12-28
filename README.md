# flask-webdev
flaskwebdevelopment2nd

## use pipenv to manage your project dependencies:
$ pipenv install

initiate virtual env with pipenv shell

pipenv install <package name>
pipenv graph to list installed packages

## Initialization for a flask App
All Flask applications must create an application instance.
from flask import Flask
app = Flask(__name__)

## Development Web Server
Flask applications include a development web server that can be started with the
flask run command.
(venv) $ export FLASK_APP=app.py
(venv) $ flask run

## Jinja control structures
chapter3 page28

## Localization of Dates and Times with Flask-Moment
https://momentjs.com/docs/#/displaying/ Moment.js documentation 