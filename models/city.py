#!/usr/bin/python3
"""
module that contain the City class

Class:
    City : define City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class that define City"""
    state_id = str("")
    name = str("")
