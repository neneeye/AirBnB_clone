#!/usr/bin/python3
"""
module that contain classes

Class:
    FileStorage : serializes instances to a JSON file
        and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances

    Functions:
        all : returns the dictionary __objects
        new : sets in __objects the obj with key <obj class name>.id
        save : serializes __objects to the JSON file
        reload : deserializes the JSON file to __objects (only if the JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects

        Return:
            the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        Arguments:
            obj : object to set in __objects

        Returns:
            None
        """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
        serializes __objects to the JSON file

        Return:
            None
        """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(dict, file, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file

        Return:
            None
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fd:
                dict_json = json.load(fd)
                for key, value in dict_json.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
