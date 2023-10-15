#!/usr/bin/python3
"""
The Base classe for AirBnB clone the console
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """str to print"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}]"

    def save(self):
        """method that updates the public instance attributes
        updated_at with the current date datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        method the returns a dictionary conatining all
        key/value of __dict__
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
