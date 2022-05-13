#!/usr/bin/env python3
""" A module that does simple obfuscation """

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, 
				 message: str, separator: str) -> str:
	""" This function performs obfuscation """
	for value in fields:
		message = re.sub(f'{value}=.*?{separator}',
					 f'{value}={redaction}{separator}', message)
	return message
	
