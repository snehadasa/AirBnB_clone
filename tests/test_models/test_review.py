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
from models.review import Review


class TestUser(unittest.TestCase):
    """unittests for Review Class"""
    def setUp(self):
        """setting up test methods"""
        pass

    def tearDown(self):
        """tests test modules"""
        pass

    def test_place_id(self):
        """test for place_id"""
        e = Review()
        e.place_id = "abc"
        self.assertEqual(type(Review.place_id), str)

    def test_user_id(self):
        """test for user_id"""
        p = Review()
        p.review = "efg"
        self.assertEqual(type(Review.user_id), str)

    def test_text(self):
        """test for text"""
        fn = Review()
        fn.text = "sneha"
        self.assertEqual(type(Review.text), str)

if __name__ == "__main__":
    unittest.main()
