#!/usr/bin/python3
"""Unittest for class BaseModel"""
import unittest
import json
import uuid
import time
import io
import contextlib
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """unittests for Place Class"""
    def setUp(self):
        """setting up test methods"""
        pass

    def tearDown(self):
        """tests test modules"""
        pass

    def test_city_id(self):
        """test for city_id"""
        e = Place()
        e.city_id = "abc"
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """test for user_id"""
        p = Place()
        p.user_id = "efg"
        self.assertEqual(type(Place.user_id), str)

    def test_name(self):
        """test for name"""
        fn = Place()
        fn.name = "sneha"
        self.assertEqual(type(Place.name), str)

    def test_description(self):
        """test for description"""
        ln = Place()
        ln.last_name = "dasa"
        self.assertEqual(type(Place.name), str)

    def test_for_number_rooms(self):
        """test for number_rooms"""
        ln = Place()
        ln.number_rooms = 2
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """test for number_bathrooms"""
        ln = Place()
        ln.number_bathrooms = 1
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_for_max_guest(self):
        """test for max_guest"""
        ln = Place()
        ln.max_guest = 4
        self.assertEqual(type(Place.max_guest), int)

    def test_for_price_by_night(self):
        """test for price by night"""
        ln = Place()
        ln.price_by_night = 120
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        """test for latitude"""
        ln = Place()
        ln.latitude = 35.67
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """test for longitude"""
        ln = Place()
        ln.longitude = 167.86
        self.assertEqual(type(Place.longitude), float)

    def test_amenity_ids(self):
        """test for amenity_ids"""
        ln = Place()
        ln.amenity_ids = "dasa"
        self.assertEqual(type(Place.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
