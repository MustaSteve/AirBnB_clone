#!/usr/bin/python3
''' the user class module'''

from models.base_model import BaseModel
'''modules to use'''


class User(BaseModel):
    '''user class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
