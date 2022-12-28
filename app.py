from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    '''
    flask-moment assumes that timestamps handled by the server-side application are 'naive' datetime objects in UTC.
    '''
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    '''
    Any additional arguments are key-value pairs that represent actual
    values for variables referenced in the template. In this example
    is receiving a name variable.
    '''
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500