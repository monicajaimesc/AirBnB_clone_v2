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
from sqlalchemy import create_engine


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None


    def __init__(self):
        # mysql is the dialect and mysqldb is the driver
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')))
        if getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)


    def delete(self, obj=None)
        """
         delete obj from the current database
        """
        if obj:
            self.__session.delete(obj)

    def save(self):
        """commits changes"""
        self.__session.commit()







