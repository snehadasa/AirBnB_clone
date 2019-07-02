#!/usr/bin/python3
"""Unittest for storage class FileStorage"""

import unittest
import json
import uuid
import time
import os
from models import storage
from modelsi.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestBase):
    """unittests for storage class FileStorage"""

    def setUp(self):
        """setting up test methods"""
        self.set = FileStorage()

    def tearDown(self):
        """tears test modules"""
        pass

    def test_save_method(self):
        attr = {"id": {"__class__": "BaseModel"}}
        self.assertEqual(type(json.dumps(attr)) is str)

    def test_for_attributes(self):
        self.assertTrue(hasattr(self.set, "name"))
        self.assertTrue(hasattr(self.set, "my_number"))
        self.assertTrue(hasattr(self.set, "created_at"))
        self.assertTrue(hasattr(self.set, "updated_at"))
        self.assertTrue(hasattr(self.set, "id"))
