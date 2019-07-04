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

    def test_for_file_path(self):
        """test cases for file_path"""
        self.assertEqual(type(storage._FileStorage__file_path), str)
        f1 = FileStorage()
        with self.assertRaises(AttributeError):
            f1.objects

    def test_for_object(self):
        """test cases for object"""
        self.assertEqual(type(storage._FileStorage__objects), dict)
        f = FileStorage()
        with self.assertRaises(AttributeError):
            f.objects

    def test_for_all(self):
        """test for function all"""
        a1 = storage.all()
        self.assertEqual(type(a1), dict)

    def test_for_all_2(self):
        """second test for all method"""
        fil = FileStorage()
        self.assertEqual(fil.all(), {})
        self.assertEqual(type(fil.all()), dict)
        fil.new(BaseModel())
        self.assertTrue(fil.all())

    def test_for_all_3(self):
        """third test for all method"""
        a1 = BaseModel()
        a2 = BaseModel()
        dic = storage.all()
        self.assertTrue("BaseModel.{}".format(a1.id) in dic)
        self.assertTrue("BaseModel.{}".format(a2.id) in dic)

    def test_for_save(self):
        """test for save function"""
        s = FileStorage()
        s._FileStorage__objects = {}
        s.new(BaseModel())
        self.assertFalse(os.path.exists("file.json"))
        s.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as f:
            self.assertEqual(type(f.read()), str)
        self.assertNotEqual(os.stat("file.json").st_size, 0)

    def test_for_new(self):
        """test for new method"""
        f = FileStorage()
        a1 = BaseModel()
        f.new(a1)
        key = "BaseModel" + "." + a1.id
        self.assertTrue(key in f.all())

    def test_for_new_with_other_types(self):
        """check for other object types"""
        f = FileStorage()
        with self.assertRaises(NameError):
            f.new(oh)
        with self.assertRaises(AttributeError):
            f.new(float("nan"))
        with self.assertRaises(AttributeError):
            f.new(12)
        with self.assertRaises(AttributeError):
            f.new("hi")
        with self.assertRaises(TypeError):
            f.new()
        with self.assertRaises(AttributeError):
            f.new([1, 2])

    def test_for_reload(self):
        """test for reload function"""
        f1 = FileStorage()
        f2 = BaseModel()
        key = "BaseModel" + "." + f2.id
        f1.new(f2)
        f1.save()
        f1._FileStorage__objects = {}
        f1.reload()
        self.assertTrue(f1.all()[key])

    def test_reload_2(self):
        """test check the reload output"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()

        all_objs = storage.all()
        self.assertEqual(storage._FileStorage__objects, all_objs)
        key = "BaseModel" + "." + my_model.id
        self.assertTrue(key in all_objs)
        self.assertEqual(type(all_objs[key]), type(BaseModel()))
        self.assertTrue(hasattr(all_objs[key], "__class__"))
        self.assertTrue(hasattr(all_objs[key], "id"))
        self.assertTrue(hasattr(all_objs[key], "created_at"))
        self.assertTrue(hasattr(all_objs[key], "updated_at"))
        self.assertTrue(hasattr(all_objs[key], "name"))
        self.assertTrue(hasattr(all_objs[key], "my_number"))


if __name__ == '__main__':
    unittest.main()
