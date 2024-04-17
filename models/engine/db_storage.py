#!/usr/bin/python3
"""
a module for the db engine storage
"""
from sqlalchemy import create_engine
from os import environ as env

user = env['HBNB_MYSQL_USER']
pwd = env['HBNB_MYSQL_PWD']
host = env['HBNB_MYSQL_HOST']
db = env['HBNB_MYSQL_DB']


class DBStorage:
	"""
	a class for instantiating the db engine
	"""

	__engine = None
	__session = None

	def __init__(self):
		"""
		instantiates new instances
		"""
		self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
