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
from models.state import State


class TestState(unittest.TestCase):
    """unittests for State Class"""
    def setUp(self):
        """setting up test methods"""
        pass

    def tearDown(self):
        """tests test modules"""
        pass

    def test_name(self):
        """test for name"""
        e = State()
        e.name = "abc"
        self.assertEqual(type(State.name), str)

if __name__ == "__main__":
    unittest.main()
