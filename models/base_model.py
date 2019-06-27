#!/usr/bin/python3
"""
a class BaseModel that defines all common attributes/methods for other classes.
"""


from uuid import uuid4
from datetime import datetime


class BaseModel():
    """class BaseModel that defines all attributes/methods for other classes"""
    def __init__(self):
        """initialize args, kwargs, id, created_at, updated_at"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """return a string"""
        s = "[{}] ({}) {}".format(self.__class__.__name__,
                                  self.id, self.__dict__)
        return s

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        d = dict()
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                d[key] = datetime.isoformat(value)
            else:
                d[key] = value
        d["__class__"] = self.__class__.__name__
        return d
