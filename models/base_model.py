#!/usr/bin/python3
""" [Principal class] """

import models
from uuid import uuid4
from datetime import datetime


datetime_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ [Base Model class]"""

    def __init__(self, *args, **kwargs):
        """[Contructor de Base Model]"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        value, datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """[toString de Base Model]"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """[updated the public instance attribute update_at]"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """[Convert to dictionary]"""
        dc = dict(self.__dict__)
        dc['__class__'] = self.__class__.__name__
        dc['updated_at'] = dc['updated_at'].isoformat()
        dc['created_at'] = dc['created_at'].isoformat()
        return dc
