#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
import os

class State(BaseModel, Base):
	""" State class """
	__tablename__ = "states"
	name = Column(String(128), nullable=False)

	if os.getenv('HBNB_TYPE_STORAGE') == 'db':
		cities = relationship('City', cascade='all, delete-orphan', back_populates="state")
	else:
		@property
		def cities(self):
			"""Returns a list of City instances"""
			from models.__init__ import storage
			cities = []
			for obj in storage.all(City).values():
				if obj.state_id == self.id:
					cities.append(obj)
			return cities
