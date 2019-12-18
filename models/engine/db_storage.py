#!/usr/bin/python3
"""

"""
import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from models import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split


class DBStorage()
    """ Create the engine for DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}"
                        .format(user, password, host, database),
                        pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all()


    def all(self, cls=None):
        """ select all the data or of any class
        """
        # Create the metadata
        get_data = self.__session()
        if cls is None:
            return get_data.query(User, State,
                                  City, Amenity, Place,
                                  Review).all()
        else:
            return get_data.query(cls).all()

    def new(self, obj):
        """ Create new object with obj
        """
        self.__session.add(obj)

    def save(self):
        """ Save all changes
        """
        self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(Session)
