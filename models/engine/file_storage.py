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
        key = "{}.{}".format(type(obj).__name__, obj.id)

    def save(self):
        """
        serializes __objects to the JSON file
        """
        serialize = {}
        for key, val in FileStoage.__objects.items():
            serialize = val.to_dict()
        with open(FileStorage.__file_path, 'w', encoding=UTF8) as fl:
            json.dump(serialize, fl)

    def reload(self):
        """deserializes file JSON to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fl:
                FileStorage.__objects.load(fl)
            for k, v in FileStorage.__objects.items():
                cl_name = v["__class__"]
                cl_name = models.classes[cl_name]
                FileStorage.__objects[key] = cl_name(**v)
        except FileNotFoundError:
            pass
