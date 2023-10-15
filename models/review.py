#!/usr/bin/python3
'''the review class module'''

from models.base_model import BaseModel
'''modules to use'''


class Review(BaseModel):
    '''review class'''

    place_id = ""
    user_id = ""
    text = ""
