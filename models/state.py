#!/usr/bin/python3
"""This is the state class"""
from models import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    
    name = Column(String(128), nullable=False)

   if os.getenv("HBNB_TYPE_STORAGE") == "db":
       
