#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, MetaData


place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
						ForeignKey('places.id'), 
						primary_key=True, 
						nullable=False),
                        Column('amenity_id', String(60),
						ForeignKey('amenities.id'), 
						primary_key=True,
						nullable=False)
						)

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
	amenities = relationship('Amenity',
						secondary='place_amenity',
                        viewonly=False,
						backref='places'
						)

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

		amenity_ids = []
		@property
		def amenities(self):
			""" Returns list of amenity ids """
			return self.amenity_ids

		@amenities.setter
		def amenities(self, obj=None):
			""" Appends amenity ids to the attribute """
			if type(obj) is Amenity and obj.id not in self.amenity_ids:
				self.amenity_ids.append(obj.id)
