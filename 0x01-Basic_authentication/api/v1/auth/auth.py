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
		bool: False """
		return False

	def authorization_header(self, request=None) -> str:
		""" auth using flask requst object """

		return None

	def current_user(self, request=None) -> TypeVar('user'):
		""" For current usage checking """

		return None
