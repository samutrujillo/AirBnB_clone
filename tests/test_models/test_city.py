#!/usr/bin/python3
""" Test Module City """
import sys
import unittest
import pep8
from models.city import City


class Test_CityModel(unittest.TestCase):
    """ Test the city model class """

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        user_path = 'models/city.py'
        result = pepstylecode.check_files([user_path])

    def setUp(self):
        self.model = City()
        self.model.save()

    def test_Amenity_initialization(self):
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.state_id, "")
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
