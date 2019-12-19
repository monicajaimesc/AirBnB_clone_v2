#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="delete", backref="my_state")
    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id
            """
            cities = []
            objects_instance = models.storage.all(City)
            for value in objects_instance.values():
                if value[id] == self.id:
                    cities.append(value)
            return cities

























       
