#!/usr/bin/env python3
"""
Main file
"""
from db import DB
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


my_db = DB()

email = 'test@test.com'
hashed_password = "hashedPwd"

user = my_db.add_user(email, hashed_password)
user2 = my_db.add_user('myt@gmail.com', hashed_password='preQQ#')
print(user.id)

try:
    my_db.update_user(user2.id, hashed_password='NewPwd')
    my_db.update_user(user.id, email='new@hbtn.com')
    print("Password updated")
except ValueError:
    print("Error")
