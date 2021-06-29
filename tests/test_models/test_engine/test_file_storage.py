#!/usr/bin/python3
""" Testing file_storage module """


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Class testing File Storage """


if __name__ == "__main__":
    unittest.main()
