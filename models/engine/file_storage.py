#!/usr/bin/python3
'''a module to Store objects'''
import os
import json
from datetime import datetime

'''json  modul'''


class FileStorage:
    '''a class that serializes instances to a JSON file
and deserializes JSON file to instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path'''

        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User, "Place\
": Place, "City": City, "State": State, "Amenity\
": Amenity, "Review": Review}
        return classes

    def reload(self):
        '''deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)'''
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name = value["__class__"]
                        obj = self.classes()[class_name](**value)
                        FileStorage.__objects[key] = obj
            except FileNotFoundError:
                pass
