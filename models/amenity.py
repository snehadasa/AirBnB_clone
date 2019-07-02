#!/usr/bin/python3
"""sub class that inherits from super class BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """public class Amenity which is set to an empty string"""
    name = ""
