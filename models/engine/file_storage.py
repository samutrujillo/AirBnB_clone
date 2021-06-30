#!/usr/bin/python3
"""All the content of the FileStorage class""" 

import json
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.city import City



class FileStorage:
    """[File storage class]"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''[return the object]'''
        return self.__objects

    def new(self, obj):
        """[add new object]"""

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """[Serializes __objects to the JSON file (path: __file_path)]"""
        for key, value in self.__objects.items():
            if not isinstance(value, dict):
                self.__objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """[deserializes the JSON file to __objects]"""
        try:
            with open(self.__file_path, "r") as file:
                serializable_file = json.load(file)
            for key, value in serializable_file.items():
                self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
