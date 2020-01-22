#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="my_state")
    else:
        name = ""

    @property
    def cities(self):
        """
        property method to get the list of cities
        :return: list of cities (instance) of the states
        """
        list_cities = []
        # city is an object and will be store in store_objects
        store_objects = models.storage.all(City)
        for key, city in store_objects.items():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
