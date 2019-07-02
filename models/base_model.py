#!/usr/bin/python3
"""
This model create a class BaseModel that defines all common attributes/methods
for other classes.
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """class BaseModel that defines all attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initialize args, kwargs, id, created_at, updated_at"""
        if not kwargs or len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    cv = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, cv)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """return a string"""
        s = "[{}] ({}) {}".format(self.__class__.__name__,
                                  self.id, self.__dict__)
        return s

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

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
