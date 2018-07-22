#!usr/bin/env python
# coding=utf8


from sqlalchemy.ext.declarative import declarative_base, declared_attr


class BaseType:
    @declared_attr
    def __table_args__(cls):
        return {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8'
        }


Base_Model = declarative_base(cls=BaseType)
