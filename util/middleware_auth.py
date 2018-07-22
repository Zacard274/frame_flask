#!/usr/bin/env python
# coding=utf8

from functools import wraps
from flask import request
from flask.globals import g
from orm import pdb


def check_auth(func):
    @wraps(func)
    def process(*arg, **kw):
        user_id = request.args.get("user_id", "")
        g.user = pdb.user.get_user_by_id(user_id)
        g.addresses = pdb.user.get_address_by_id(user_id)
        for i in g.addresses:
            print(i)
        return func(*arg, **kw)

    return process
