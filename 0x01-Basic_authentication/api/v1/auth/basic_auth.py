#!/usr/bin/env python3
""" Basic authentication class """

from api.v1.auth.auth import Auth

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
