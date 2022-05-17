#!/usr/bin/env python3
""" A module that performs password encrypting
using bycrypt lib in python """

import bcrypt
from typing import List

def hash_password(password: str):
	""" Function that hashes a password """
	passw = bytes(password, 'utf-8')
	encr = bcrypt.hashpw(passw, bcrypt.gensalt())
	
	return encr

def is_valid(hashed_password: bytes, password: str):
	""" Checks password validity """
	password = bytes(password, 'utf-8')
	res = bcrypt.checkpw(password, hashed_password)
	return res
