#!/usr/bin/env python
# coding=utf8

from flask import Flask
from middleware import midlogger
from config import DEV_MODE
from handler.user import user
from orm import pdb

app = Flask(__name__)
# use middleware
app.wsgi_app = midlogger.LoggerMiddleware(app.wsgi_app)
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    pdb.create_all()
    app.run(debug=DEV_MODE)
