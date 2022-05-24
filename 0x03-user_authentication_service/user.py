#!/usr/bin/env python3
""" A module for creating a table in a database
named user using sqlalchemy declarative mapping. """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import Sequence


Base = declarative_base()


class User(Base):
    """ A class that inherits from sqlalchemy base
    declarative class """
    __tablename__ = 'users'

    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email, hashed_password):
        """ constructor """
        self.email = email
        self.hashed_password = hashed_password


    def __rpre__(self):
        """ Class formal description """
        s = "email:{} and session_id:{}".format(self.email, self.session_id)
        return s
