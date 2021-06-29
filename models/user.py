#!/usr/bin/python3
from models.base_model import BaseModel
""" Module for class Review """


class User(BaseModel):
    """
    class User - classes that inherit from BaseModel.

    Args:
        BaseModel (class): parent class.
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
