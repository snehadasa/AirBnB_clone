#!/usr/bin/python3
"""sub class that inherits from super class BaseModel"""

from models.base_model import BaseModel

class State(BaseModel):
    """public class attribute name which is set to an empty string"""
    name = ""
