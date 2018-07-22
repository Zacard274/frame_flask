#!/usr/bin/env python
# coding=utf8


from .Base import Base_Model
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR


class AddressModel(Base_Model):
    __tablename__ = 'addresses'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(INTEGER(11), ForeignKey("users.id"))
    address = Column(VARCHAR(256))

    def __repr__(self):
        return f"<address : {self.address}>"


class AddressOrm:
    def __init__(self, pdb):
        self.db = pdb
        self.engine = pdb.get_engine

