#!/usr/bin/env python
# coding=utf8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from .User import UserOrm
from .Email import EmailOrm
from .Address import AddressOrm
from .Base import Base_Model


# 这里我使用的是PyMySQL
# echo=True是开启调试，这样当我们执行文件的时候会提示相应的文字
class Orm:
    def __init__(self):
        self._engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/blog', echo=True)
        self.__session_init()
        self.user = UserOrm(self)
        self.email = EmailOrm(self)
        self.address = AddressOrm(self)

    def __session_init(self):
        self.session = scoped_session(sessionmaker(bind=self._engine))()
        return

    def get_session(self):
        return self.session

    def get_engine(self):
        return self._engine

    def get_connection(self):
        # if you want use transaction
        return self._engine.connect()

    def create_all(self):
        Base_Model.metadata.create_all(self._engine)


pdb = Orm()
