#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="my_state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        init method, new object (state) created from BaseModel Class
        :param args: used to pass a variable number of arguments
        :param kwargs: dictionary or keyword arguments
        """
        # super() to call the __init__() from BaseModel Class
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """
        property method to get the list of cities
        :return: list of cities (instance) of the states
        """
        list_cities = []
        # city is an object and will be store in store_objects
        store_objects = models.storage.all(models.city)
        for city in store_objects:
            if city.citi.state_id == self.id:
                list_cities.append(city)
        return list_cities
