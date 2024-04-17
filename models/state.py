#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
