#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("mysql://la2:afusat123#@0.0.0.0/hbtn1",
                                     echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add a user """
        user = User(email, hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs):
        """Find a user method """
        for name, val in kwargs.items():
            if name in vars(User):
                query = self._session.query(User).filter_by(
                        **{name: val}).first()
                if query is None:
                    raise NoResultFound
                return query
            else:
                raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Updates a user with user_id """
        query = self.find_user_by(id=user_id)
        if query is None:
            raise NoResultFound
        for name, val in kwargs.items():
            setattr(query, name, val)
        self._session.add(query)
        self._session.commit()
        return None
