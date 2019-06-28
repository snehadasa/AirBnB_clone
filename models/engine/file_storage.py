#!/usr/bin/python3
"""serialises instances to a json file"""


import json


class FileStorage():
    """class FileStorage"""

    def __init__(self):
        self.file_path = "file.json"
        self.objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.__objects = value

    def all(self):
        return self.objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes the json file to objects"""
        for key, value in self.__objects.items():
            if type(value) is not dict:

        name = self.__file_path
        with open(name, mode="w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes json file to objects"""

