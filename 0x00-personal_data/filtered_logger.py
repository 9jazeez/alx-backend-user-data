#!/usr/bin/env python3
""" A module that does simple obfuscation """

import re
from typing import List
import logging

PII_FIELDS = ("name", "phone", "password", "email", "ssn")

def filter_datum(fields: List[str], redaction: str, 
				 message: str, separator: str) -> str:
	""" This function performs obfuscation """
	for value in fields:
		message = re.sub(f'{value}=.*?{separator}',
					 f'{value}={redaction}{separator}', message)
	return message

def get_logger() -> logging.Logger:
	""" A logger with filter format """
	logger = logging.getLogger('user_data')
	logger.propagate = False
	logger.setLevel(logging.INFO)

	str_handler = logging.StreamHandler()
	str_handler.setLevel(logging.INFO)
	str_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
	logger.addHandler(str_handler)

	return logger


class RedactingFormatter(logging.Formatter):
	""" Redacting Formatter class
	"""

	REDACTION = "***"
	FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
	SEPARATOR = ";"

	def __init__(self, fields: List[str]):
		"""Class Constructor """
		super(RedactingFormatter, self).__init__(self.FORMAT)
		self.fields = fields

	def format(self, record: logging.LogRecord) -> str:
		""" Implement a filter function using filter_datum """
		record.msg = filter_datum(self.fields, self.REDACTION,
								  record.getMessage(), self.SEPARATOR)
		return super(RedactingFormatter, self).format(record)

