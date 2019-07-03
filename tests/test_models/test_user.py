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
from models.user import User


class TestUser(unittest.TestCase):
    """unittests for User Class"""
    def setUp(self):
        """setting up test methods"""
        pass

    def tearDown(self):
        """tests test modules"""
        pass

    def test_email(self):
        """test for email"""
        e = User()
        e.email = "abc"
        self.assertEqual(type(e.email), str)

    def test_password(self):
        """test for password"""
        p = User()
        p.password = "efg"
        self.assertEqual(type(p.password), str)

    def test_first_name(self):
        """test for first_name"""
        fn = User()
        fn.first_name = "van"
        self.assertEqual(type(fn.first_name), str)

    def test_last_name(self):
        """test for last_name"""
        ln = User()
        ln.last_name = "phan"
        self.assertEqual(type(ln.last_name), str)

if __name__ == "__main__":
    unittest.main()
