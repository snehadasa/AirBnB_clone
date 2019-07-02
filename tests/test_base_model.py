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
