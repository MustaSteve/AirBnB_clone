#!/usr/bin/python3
<<<<<<< HEAD
"""
class User that inherits fro BaseModel
"""
from models.basemodel import BaseModel


class User(BaseModel):
    """all public class attributes"""
=======
''' the user class module'''

from models.base_model import BaseModel
'''modules to use'''


class User(BaseModel):
    '''user class'''

>>>>>>> ed407161745b016a92e3b168f5cff3cf6c9ebef6
    email = ""
    password = ""
    first_name = ""
    last_name = ""
