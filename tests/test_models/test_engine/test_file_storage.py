#!/usr/bin/python3
"""This Unittest for storage class FileStorage"""

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
        self.assertEqual(type(a1), dict)
        for k, v in a1.items():
            self.assertEqual(type(v), type(a))

    def test_for_all_2(self):
        """second test for all method"""
        fil = FileStorage()
        self.assertEqual(fil.all(), {})
        self.assertEqual(type(fil.all()), dict)
        fil.new(BaseModel())
        self.assertTrue(fil.all())

    def test_for_save(self):
        """test for save function"""
        s = FileStorage()
        s.new(BaseModel())
        self.assertFalse(os.path.exists("file.json"))
        s.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as f:
            self.assertEqual(type(f.read()), str)
        self.assertNotEqual(os.stat("file.json").st_size, 0)

    def test_for_new(self):
        """test for new method"""
        a1 = BaseModel()
        a2 = BaseModel()
        dic = storage.all()
        self.assertTrue("BaseModel.{}".format(a1.id) in dic)
        self.assertTrue("BaseModel.{}".format(a2.id) in dic)

    def test_for_new_with_other_types(self):
        """check for other object types"""
        f = FileStorage()
        with self.assertRaises(NameError):
            f.new(oh)
        with self.assertRaisesRegex(AttributeError,
                                    "'float' object has no attribute 'id'"):
            f.new(float("nan"))
        with self.assertRaisesRegex(AttributeError,
                                    "'int' object has no attribute 'id'"):
            f.new(12)
        with self.assertRaisesRegex(AttributeError,
                                    "'str' object has no attribute 'id'"):
            f.new("hi")
        with self.assertRaises(TypeError):
            f.new()
        with self.assertRaisesRegex(AttributeError,
                                    "'list' object has no attribute 'id'"):
            f.new([1, 2])

    def test_for_reload(self):
        """test for reload function"""
        f1 = FileStorage()
        f2 = BaseModel()
        key = "BaseModel" + "." + f2.id
        f1.new(f2)
        f1.save()
        f1.__objects = {}
        f1.reload()
        self.assertTrue(f1.all()[key])
