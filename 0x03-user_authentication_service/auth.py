#!/usr/bin/env python3
""" A module that uses bcrypt to hash
    a password of bytes """

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Takes a password str and hash it to a
        bytes type encoded """
    passw = bytes(password, 'utf-8')
    hash_pw = bcrypt.hashpw(passw, bcrypt.gensalt())
    return hash_pw
