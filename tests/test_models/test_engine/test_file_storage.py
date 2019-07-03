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
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """tears test modules"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_for_all(self):
        """test for function all"""
        a = BaseModel()
        a1 = storage.all()
        for k, v in a1.items():
            self.assertEqual(type(v), type(a))

    def test_for_save(self):
        c = BaseModel()
        c.name = "Holberton"
        c.my_number = 89
        c.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as f:
            self.assertEqual(type(f.read()), str)
