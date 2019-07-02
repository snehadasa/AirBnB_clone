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


class TestBaseModel(unittest.TestCase):
    """unittests for BaseModel class"""

    def setUp(self):
        """setting up test methods"""
        self.b1 = BaseModel()

    def tearDown(self):
        """tests test modules"""
        pass

    def test_class_type(self):
        """tests for correct class type"""
        my_object = BaseModel()
        self.assertEqual(my_object.__class__.__name__, "BaseModel")

    def test_to_dict(self):
        """tests for isinstance and is sub class of the superclass"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)
        self.assertTrue(issubclass(type(my_object), BaseModel))

    def test_for_BaseModel(self):
        """test for instance creation"""
        my_object = BaseModel()

    def test_for_args(self):
        """tests to check for attributes if present"""
        my_object = BaseModel()
        self.assertTrue(hasattr(my_object, "id"))
        self.assertTrue(hasattr(my_object, "created_at"))
        self.assertTrue(hasattr(my_object, "updated_at"))

    def test_to_invalid_args(self):
        """test to check for invalid argument"""
        with self.assertRaises(TypeError):
            my_object = BaseModel(**"Holberton")

    def test_to_wrong_args(self):
        """test to check for wrong args being passed"""
        with self.assertRaises(TypeError):
            my_object = BaseModel(**"Holber")

    def test_to_wrong_type(self):
        """test to check for passing int"""
        with self.assertRaises(TypeError):
            my_object = BaseModel(**12)

    def test_to_wrong_type_float(self):
        """test to check for passing float"""
        with self.assertRaises(TypeError):
            my_object = BaseModel(**5.2)

    def test_wrong_type_for_args(self):
        """test to check for passing float"""
        with self.assertRaises(ValueError):
            my_object = BaseModel(**float("betty"))

    def test_for_empty_dict(self):
        """test to check for attributes in the dict"""
        my_object = BaseModel(**{})
        self.assertTrue(hasattr(my_object, "id"))
        self.assertTrue(hasattr(my_object, "created_at"))
        self.assertTrue(hasattr(my_object, "updated_at"))

    def test_for_args(self):
        """tests to check for different parameters"""
        with self.assertRaises(TypeError):
            my_object = BaseModel(**[])
            my_object = BaseModel(**15)
            my_object = BaseModel(**24.66)
            my_object = BaseModel(**"sneha")
            self.assertTrue(hasattr(my_object, "id"))
            self.assertTrue(hasattr(my_object, "created_at"))
            self.assertTrue(hasattr(my_object, "updated_at"))

    def test_for_datetime(self):
        """test to check for datetime diff"""
        my_object = BaseModel()
        date = datetime.now()
        time_diff = my_object.updated_at - my_object.created_at
        self.assertTrue(abs(time_diff.total_seconds()) < 0.01)

    def test_for_datetime(self):
        """test to check for approx time diff"""
        my_object = BaseModel()
        date = datetime.now()
        time_diff = my_object.created_at - my_object.updated_at
        self.assertTrue(abs(time_diff.total_seconds()) < 0.1)

    def test_to_string(self):
        """test to check for correct string being passed"""
        my_object = BaseModel()
        s = "[{}] ({}) {}".format(my_object.__class__.__name__,
                                  my_object.id, my_object.__dict__)
        self.assertEqual(s, str(my_object))

    def test_for_uuid(self):
        """test to check for correct uuid"""
        my_object = BaseModel()
        self.assertTrue(my_object.id)

    def test_for_updated_at(self):
        """test to check for correct updated_at"""
        my_object = BaseModel()
        self.assertTrue(my_object.updated_at)

    def test_for_created_at(self):
        """test to check for correct created_at"""
        my_object = BaseModel()
        self.assertTrue(my_object.created_at)

if __name__ == "__main__":
    unittest.main()
