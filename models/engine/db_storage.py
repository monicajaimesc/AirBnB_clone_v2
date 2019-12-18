#!/usr/bin/python3
"""
DBStorage: database management system (DBMS) uses to create,
read, update and delete (CRUD) data from a database.
"""
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy as db



class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None


    def __init__(self):
        # mysql is the dialect and mysqldb is the driver
        self.__engine = db.create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')))
        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

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
        """commits changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """
         delete obj from the current database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(Session)
