#!/usr/bin/env python
# coding=utf8


from .Base import Base_Model
from sqlalchemy import Column, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR
from util.tools import model_to_dict


class UserModel(Base_Model):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(64))
    address = relationship("AddressModel", backref="_user", lazy="select")
    email = relationship("EmailModel", backref="_user", lazy="select")
    password = Column(VARCHAR(256))


class UserOrm:
    def __init__(self, pdb):
        self.db = pdb
        self.engine = pdb.get_engine()
        self.session = pdb.get_session()

    def get_user_by_id(self, user_id):
        statement = text('select * from users where id = :id ')
        param = {'id': user_id}
        return self.engine.execute(statement, param).fetchall()

    @model_to_dict
    def get_address_by_id(self, user_id):
        result = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        return result
