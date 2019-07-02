#!/usr/bin/python3
"""Unittest for storage class FileStorage"""

import unittest
import json
import uuid
import time
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """unittests for storage class FileStorage"""

    def setUp(self):
        """setting up test methods"""
        self.set = FileStorage()

    def tearDown(self):
        """tears test modules"""
        pass

    def test_save_method(self):
        """test to check for the attr is string"""
        attr = {"id": {"__class__": "BaseModel"}}
        self.assertTrue(type(json.dumps(attr)) is str)

    def test_for_attributes(self):
        """test to check for the correct attribute"""
        self.assertFalse(hasattr(self.set, "name"))
        self.assertFalse(hasattr(self.set, "my_number"))
        self.assertFalse(hasattr(self.set, "created_at"))
        self.assertFalse(hasattr(self.set, "updated_at"))
        self.assertFalse(hasattr(self.set, "id"))
