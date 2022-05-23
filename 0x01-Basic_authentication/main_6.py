#!/usr/bin/env python3
""" Main 6
"""
import base64
from api.v1.auth.basic_auth import BasicAuth
from models.user import User

""" Create a user test """
user_email = "Fashmd@gmail.com"
user_clear_pwd = "H0lberto3RR24!"
first = "Fash"
last = "Funmi"
user = User()
user.email = user_email
user.password = user_clear_pwd
user.first_name = first
user.last_name = last

print("New user:{} with {} / {}".format(user.first_name,
										user.id, user.display_name()))
user.save()

basic_clear = "{}:{}".format(user_email, user_clear_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))
