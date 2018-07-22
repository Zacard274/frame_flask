#!/usr/bin/env python
# coding=utf8

from flask import Blueprint
from flask.globals import g
from util.middleware_auth import check_auth

user = Blueprint("user", __name__)


@user.route("/", methods=["GET"])
@check_auth
def get_all_user():
    print("result =====", g.user)
    return "test"

