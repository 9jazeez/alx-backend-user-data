#!/usr/bin/env python3
""" A module that does simple obfuscation """

import re
from typing import List
import logging
from os import environ
import mysql.connector

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

def get_db() -> mysql.connector.connection.MySQLConnection:
	""" A function that connects to mysql db """
	user_name = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
	pass_word = environ.get("PERSONAL_DATA_DB_PASSWORD", " ")
	host_name = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
	db_name = environ.get("PERSONAL_DATA_DB_NAME")

	conn = mysql.connector.connection.MySQLConnection(user=user_name,
													  password=pass_word,
													  host=host_name,
													  database=db_name)
	return conn


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

def main():
	""" This function obtains a database connection using get_db
	then retrieves all rows in the users table and display each
	row under a filtered format. """
	
	db = get_db()
	cursor = db.cursor()
	cursor.execute("SELECT * FROM users;")
	fields = [i[0] for i in cursor.description]
	
	logger = get_logger()

	for row in cursor:
		row_str = ''.join(f'{val}={str(r)};' for r,  val in zip(row, fields)
		logger.info(row_str.strip())

	cursor.close()
	db.close()

if __name__ == '__main__':
	main()

