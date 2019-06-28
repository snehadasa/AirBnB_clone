#!/usr/bin/python3
"""class baseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """str representation of the base model"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance attribute with the current time"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """dictionary representation of all keys/values associated with __dict__"""
        dic = dict()
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dic[key] = datetime.isoformat(value)
            else:
                dic[key] = value
        dic["__class__"] = self.__class__.__name__
        return dic
