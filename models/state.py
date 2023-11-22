#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City

class State(BaseModel, Base):
	""" State class """
	__tablename__ = "states"
	name = Column(String(128), nullable=False)
	cities = relationship('City', back_populates="state")

	@property
	def cities(self):
		"""Returns a list of City instances"""
		from models.__init__ import storage
		cities = []
		for key, obj in storage.all(City).items():
			if obj.id == self.id:
				cities.append(obj)
			return cities
