#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models
from models.base_model import BaseModel, Base

STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref='states', cascade='all, delete-orphan')

    if STORAGE_TYPE != 'db':
        name = ""
        cities = []
        @property
        def cities(self):
            """
            return all cities
            """
            city_list = []

            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
