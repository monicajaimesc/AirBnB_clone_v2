#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
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
        cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        "returns the list of City instances with state_id"
        cities = []
        objects_instance = models.storage.all("city")

        for value in objects_instance:
            if value.id == self.id:
                cities.append(objects_instance[value])
        return cities

























       
