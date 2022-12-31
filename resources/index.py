# from flask.views import MethodView
# # from flask_bootstrap.forms import NameForm
# from flask_smorest import Blueprint, abort
# from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt, jwt_required
# from passlib.hash import pbkdf2_sha256
# from flask_bootstrap import Bootstrap
# # from .forms import NameForm
# # import requests
# import os
# from sqlalchemy import or_
# import redis
# # from rq import Queue
# # from tasks import send_user_registration_email
#
# from db import db
# from models import UserModel
# from schemas import UserSchema, UserRegisterSchema
# from blocklist import BLOCKLIST
# from flask import render_template
# from datetime import datetime
#
# blp = Blueprint("Index", 'index', description="index")
#
# @blp.route('/', methods=['GET','POST'])
# class Index(MethodView):
#     @blp.response(200, UserSchema)
#     def get(self):
#         '''
#         flask-moment assumes that timestamps handled by the server-side application are 'naive' datetime objects in UTC.
#         '''
#         name=None
#         form = NameForm()
#         if form.validate_on_submit():
#             name = form.name.data
#             form.name.data = ''
#         return {render_template('index.html', current_time=datetime.utcnow(
#
#         ), form=form, name=name)}, 200
#
#     # @blp.route('/user/<name>')
#     # def user(name):
#     #     '''
#     #     Any additional arguments are key-value pairs that represent actual
#     #     values for variables referenced in the template. In this example
#     #     is receiving a name variable.
#     #     '''
#     #     return {render_template('user.html', name=name)}, 200
