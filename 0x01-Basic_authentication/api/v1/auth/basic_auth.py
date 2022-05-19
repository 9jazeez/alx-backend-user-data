#!/usr/bin/env python3
""" Basic authentication class """

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User

class BasicAuth(Auth):
	""" Basic auth class """
	def extract_base64_authorization_header(self, 
											authorization_header: str
											) -> str:
		""" Method that returns the Base64 part of auth
			header for basic auth """
		if authorization_header is None:
			return None
		if not isinstance(authorization_header, str):
			return None
		if not authorization_header.startswith("Basic "):
			return None
		base64_res = authorization_header.split(' ')
		
		return base64_res[1]

	def decode_base64_authorization_header(self,
											base64_authorization_header: str
											) -> str:
		""" Method that return decoded value of base64 string
			of base64_authorization_header """
		inpt = base64_authorization_header
		if inpt is None:
			return None
		if not isinstance(inpt, str):
			return None
		try:
			base_enc = inpt.encode('utf-8')
			base_dec = base64.b64decode(base_enc)
			result = base_dec.decode('utf-8')
			return result
		except Exception:
			return None 

	def extract_user_credentials(self,
								 decoded_base64_authorization_header: str
								 ) -> (str, str):
		""" This method gets the user credentials from
			base64_authorization header and returns
			a tuple """
		dec_val = decoded_base64_authorization_header
		if dec_val is None:
			return (None, None)
		if not isinstance(dec_val, str):
			return (None, None)
		if ':' not in dec_val:
			return (None, None)
		cre = dec_val.split(':', 1)

		return (cre[0], cre[1])

	def user_object_from_credentials(self, user_email: str,
									 user_pwd: str) -> TypeVar('User'):
		""" This method returns user instance based on the credentials """
		if user_email is None or not isinstance(user_email, str):
			return None
		if user_pwd is None or not isinstance(user_pwd, str):
			return None
		try:
			users = User.search({'email': user_email})
			for user in users:
				if user.is_valid_password(user_pwd):
					return user
		except Exception:
			return None

	def current_user(self, request=None) -> TypeVar('User'):
		""" Overloaded Auth's current_user and returns the
			User instance """
		try:
			header = self.authorization_header(request)
			base64H = self.extra_base64_authorization_header(header)
			decodeVal = self.decode_base64_authorization_header(base64H)
			credentials = self.extract_user_credentials(decodeVal)
			user = self.user_object_from_credentials(credentials[0],
													 credentials[1])
			return user
		except Exception:
			return None
