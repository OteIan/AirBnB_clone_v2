#!/usr/bin/bash
"""New storage"""
import os
from models.base_model import Base
from sqlalchemy import create_engine, create_all
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
	"""Database storage"""
	__engine = None
	__session = None

	def __init__(self):
		self.__engine = create_engine(
			'mysql+mysqldb://{}:{}@{}:3306/{}'.
			format(
				os.getenv('HBNB_MYSQL_USER'),
				os.getenv('HBNB_MYSQL_PWD'),
				os.getenv('HBNB_MYSQL_HOST'),
				os.getenv('HBNB_MYSQL_DB'),
				pool_pre_ping=True
		        )
		)
		if os.getenv('HBNB_ENV') == 'test':
			Base.metadata.drop_all(self.__engine)
		
		self.__session = scoped_session(sessionmaker(bind=self.__engine,
                    expire_on_commit=False))
                Base.metadata.create_all(self.__engine)

	def all(self, cls=None):
		""""Query on the current database session all 
		objects depending on class name"""
		from models.user import User
		from models.place import Place
		from models.state import State
		from models.city import City
		from models.amenity import Amenity
		from models.review import Review
		classes = [User, State, City, Amenity, Place, Review]
		if (cls != None):
			classes = [cls]
		objects = {}
		for cls in classes:
			query = self.__session.query(cls)
			for obj in query:
				key = "{}.{}".format(type(obj).__name__, obj.id)
				objects[key] = obj

		return objects
	
	def new(self, obj):
		""""""
		self.__session.add(obj)
	
	def save(self):
		""""""
		self.__session.commit()

	def delete(self, obj=None):
		""""""
		if obj != None:
			self.__session.delete(obj)

	def reload(self):
		""""""
		Base.metadata.create_all(self.__engine)
		self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

