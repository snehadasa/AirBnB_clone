#!/usr/bin/python3
"""Unittest for class BaseModel"""

import unittest
import json
import uuid
import time
import os
from models import storage
from modelsi.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestBase):
    """unittests for BaseModel class"""

    def setUp(self):
        """setting up test methods"""
        pass

    def tearDown(self):
        """tears test modules"""
        pass

    def test_class_type(self):
        cl = BaseModel()
        self.assertEqual(cl.__class__.__name__, "BaseModel")

    def test_to_dict(self):
        cl = BaseModel()
        self.assertIsInstane(cl, BaseModel)
        self.assertTrue(issubclass(type(cl), BaseModel))

    def test_to_kwargs(self):
        self.assertNotEqual(len(kwargs), 0)

    def test_for_args(self):
        my_object = Basemodel()
        self.assertTrue(hasattr(my_object, "id"))
        self.assertTrue(hasattr(my_object, "created_at"))
        self.assertTrue(hasattr(my_object, "updated_at"))

    def test_to_invalid_args(self):
        with self.assertRaises(TypeError):
        my_object = BaseModel(*/"Holberton")

    def test_to_wrong_args(self):
        with self.assertRaises(TypeError):
        my_object = BaseModel(**Holber)

    def test_to_wrong_type(self):
        with self.assertRaises(TypeError):
        my_object = BaseModel(**12)

    def test_to_wrong_type_float(self):
        with self.assertRaises(TypeError):
        my_object = BaseModel(**5.2)

    def test_wrong_type_for_args(self):
        with self.assertRaises(TypeError):
        my_object = BaseModel(**float("betty"))

    def test_for_empty_dict(self):
        my_object = BaseModel(**{})
        self.assertTrue(hasattr(my_object, "id"))
        self.assertTrue(hasattr(my_object, "created_at"))
        self.assertTrue(hasattr(my_object, "updated_at"))

    def test_for_datetime_format(self):
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(date_format, )

    def test_to_string(self):
        my_object = BaseModel()
        s = "[{}] ({}) {}".format(my_object.__class__.__name__,
                                  my_object.id, my_object.__dict__)
        self.assertEqual(s, str(my_object))

    def test_for_uuid(self):
        my_object = BaseModel()
        self.assertTrue(my_object.id)

    def test_to_json_file(self):
        my_object = BaseModel()
        date = datetime.now()
        my_object.save()


if __name__ == "__main__":
    unittest.main()
