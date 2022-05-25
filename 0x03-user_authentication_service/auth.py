#!/usr/bin/env python3
""" A module that uses bcrypt to hash
    a password of bytes """

import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
import uuid


def _hash_password(password: str) -> bytes:
    """ Takes a password str and hash it to a
        bytes type encoded """
    passw = bytes(password, 'utf-8')
    hash_pw = bcrypt.hashpw(passw, bcrypt.gensalt())
    return hash_pw


class Auth:
    """ Class for authentication """

    def __init__(self):
        """ Class constructor """
        self._db = DB()

    def register_user(self, email: str, password: str):
        """ User registration """
        try:
            query = self._db.find_user_by(email=email)
            if query.email == email:
                raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            password = _hash_password(password)
            user = self._db.add_user(email, password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ User credential validation """
        try:
            query = self._db.find_user_by(email=email)
            if query.email == email:
                password = bytes(password, 'utf-8')
                hashed = bytes(query.hashed_password, 'utf-8')
                ps_ch = bcrypt.checkpw(password, hashed)
                return ps_ch
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """ UUID generator """
        _id_u = uuid.uuid4()
        return _id_u

    def create_session(self, email: str) -> str:
        """ Session creation method """
        try:
            query = self._db.find_user_by(email=email)
            if query.email == email:
                session = self._generate_uuid()
                self._db.update_user(query.id, session_id=session)
                return session
        except NoResultFound:
            return None
