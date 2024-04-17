#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place")
