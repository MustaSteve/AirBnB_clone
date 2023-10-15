#!/usr/bin/python3
"""
class to serializes instances to JSON file and deserializes
JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    all class attributes and instances methods to serialize and
    deserialize fil
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """method to set __objects with his key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        dict_value = obj
        FileStorage.__objects[key] = dict_value

    def save(self):
        """
        serializes __objects to the JSON file
        """
        for key, value in FileStorage.__objects.items():
            dict_obj[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding=UTF8) as fl:
            json.dump(dict_obj, fl)

    def 
