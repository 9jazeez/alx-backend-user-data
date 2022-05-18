#!/usr/bin/env python3
""" A module for managing API authentication """

from typing import List, TypeVar
from flask import request, abort


class Auth():
	""" A class for managing an API 
	authentication """

	def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
		""" A public method for authentication 
		Returns
		bool: False or True """
		if path is None or excluded_paths is None or not len(excluded_paths):
			return True
		if path[-1] != '/':
			path += '/'
		for val in excluded_paths:
			if val.endswith('*'):
				if path.startswith(val[:1]):
					return False
		if path in excluded_paths:
			return False
		else:
			return True

	def authorization_header(self, request=None) -> str:
		""" auth using flask requst object """

		return None

	def current_user(self, request=None) -> TypeVar('user'):
		""" For current usage checking """

		return None
