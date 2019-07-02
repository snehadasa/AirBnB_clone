#!/usr/bin/python3
"""sub class City that inherits from super class BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """public class attribute name which is set to an empty string"""
    name = ""
    state_id = ""
