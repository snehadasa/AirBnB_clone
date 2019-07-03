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
from models.city import City


class TestCity(unittest.TestCase):
    """unittests for City Class"""
    def setUp(self):
        """setting up test methods"""
        pass

    def tearDown(self):
        """tests test modules"""
        pass

    def test_name(self):
        """test for name"""
        e = City()
        e.name = "abc"
        self.assertEqual(type(City.name), str)

    def test_state_id(self):
        """test for state_id"""
        ln = City()
        ln.state_id = "sneha"
        self.assertEqual(type(City.state_id), str)

if __name__ == "__main__":
    unittest.main()
