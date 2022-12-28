from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_smorest import abort, Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from datetime import datetime
# import requests
from dotenv import load_dotenv
import os

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint

# from db import stores, items
from db import db
import models

from blocklist import BLOCKLIST


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()

    # app.config['SECRET-KEY'] = 'super hard string'
    
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    bootstrap = Bootstrap(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    moment = Moment(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "chacotasprod" #change this secrets.SystemRandom().getrandbits(128)
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}


    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @app.before_first_request
    def create_tables():
        with app.app_context():
            db.create_all()
        # db.create_all()

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

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app