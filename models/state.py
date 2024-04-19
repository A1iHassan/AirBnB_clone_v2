#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import os
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    # For DBStorage
    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")

    # For FileStorage
    else:
        @property
        def cities(self):
            """Getter attribute for cities"""
            from models.__init__ import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
