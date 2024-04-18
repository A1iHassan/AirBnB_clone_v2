#!/usr/bin/python3
"""
a module for the db engine storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ as env
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

try:
	user = env['HBNB_MYSQL_USER']
	pwd = env['HBNB_MYSQL_PWD']
	host = env['HBNB_MYSQL_HOST']
	db = env['HBNB_MYSQL_DB']
	Env = env['HBNB_ENV']
except KeyError:
  pass


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
		Base.metadata.reflect(self.__engine)
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		self.__session = scoped_session(session_factory)
		if Env == 'test':
			Base.metadata.drop_all(self.__engine)

	def all(self, cls=None):
		"""
		queries objects from db
		"""
		if cls:
			objects = self.__session.query(cls).all()
		else:
			objects = []
			for model in [User, State, City, Amenity, Place, Review]:
				objects.extend(self.__session.query(model).all())
		return {f"{type(obj).__name__}.{obj.id}": obj for obj in objects}

	def new(self, obj):
		"""
  	add the object to the current database session
		"""
		self.__session.add(obj)

	def save(self):
		"""
		commit all changes of the current database session
  	"""
		self.__session.commit()

	def delete(self, obj=None):
		"""
		delete from the current database session
  	"""
		if obj:
			self.__session.delete(obj)

	def reload(self):
		"""
		create all tables in the database and create the current database session
  	"""
		Base.metadata.reflect(self.__engine)
		Base.metadata.create_all(self.__engine)
		session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		self.__session = scoped_session(session_factory)
