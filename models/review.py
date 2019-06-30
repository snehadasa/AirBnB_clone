#!/usr/bin/python3
"""sub class that inherits from super class BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """public class attribute Review which is set to an empty string"""
    place_id = ""
    user_id = ""
    text = ""
