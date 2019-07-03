#!/usr/bin/python3
"""serialises instances to a json file"""


import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects to an obj with a key (object class name).id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes the json file to objects(json.dumps)"""
        name = self.__file_path
        with open(name, mode="w") as f:
            dic = dict()
            for key, value in self.__objects.items():
                if type(value) is not dict:
                    dic[key] = value.to_dict()
            json.dump(dic, f)

    def reload(self):
        """deserializes json file to objects(json.loads)"""
        name = self.__file_path
        if os.path.exists(name):
            with open(name, mode="r") as f:
                a = json.loads(f.read())
            b = dict()
            for key, value in a.items():
                b[key] = eval(a[key]["__class__"])(**value)
            self.__objects = b
