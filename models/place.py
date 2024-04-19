#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
import os
metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60), ForeignKey('amenities.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey('places.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
                          )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    id = Column(Integer, primary_key=True)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(Integer, primary_key=True)
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        user = relationship("User", backref="places")
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False, default=0.0)
        longitude = Column(Float, nullable=False, default=0.0)
        cities = relationship("City")
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Place")
        place_id = Column(String(60), nullable=False)
        amenity_ids = Column(String(60), nullable=False)
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = ''
        number_bathrooms = ''
        max_guest = ''
        price_by_night= ''
        latitude=''
        longitude=''
        amenities=''

    @property
    def amenities(self):
        """"getter attribute returns list of amenty instance"""
        from models.amenity import Amenity
        Amenity_list = []
        all_amenities = models.storage.all(Amenity)
        for amenity in all_amenities.values():
            if amenity.id in self.amenity_ids:
                Amenity_list.append(amenity)
        return Amenity_list