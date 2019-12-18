#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    # from models.engine.db_storage import DBStorage
    # create an instance of DBSstorage store it in storage
    storage = DBStorage()
    storage.reload()
else:
    # from models.engine.file_storage import FileStorage
    # create an instance of FileStorage and store it in the variable storage
    storage = FileStorage()
    storage.reload()
