#!/usr/bin/python3
"""
class User that inherits fro BaseModel
"""
from models.basemodel import BaseModel


class User(BaseModel):
    """all public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
