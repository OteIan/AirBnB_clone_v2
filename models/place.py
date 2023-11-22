#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
	""" A place to stay """
	__tablename__ = "places"
	city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
	user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
	name = Column(String(128), nullable=False)
	description = Column(String(1024), nullable=True)
	number_rooms = Column(Integer, nullable=False, default=0)
	number_bathrooms = Column(Integer, nullable=False, default=0)
	max_guest = Column(Integer, nullable=False, default=0)
	price_by_night = Column(Integer, nullable=False, default=0)
	latitude = Column(Float, nullable=True)
	longitude = Column(Float, nullable=True)
	reviews = relationship('Review', cascade='all, delete-orphan', backref='place')

	if getenv('HBNB_TYPE_STORAGE') == 'FileStorage':
		@property
		def reviews(self):
			"""
			Returns the list of Review instances with place
            """
			from models.__init__ import storage
			reviews = []
			for obj in storage.all(Review).values():
				if obj.place_id == self.id:
					reviews.append(obj)
			return reviews
