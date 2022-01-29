#!/usr/bin/python3
"""
Contains the subclass City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ creates an instance of a City"""
    state_id = ""
    name = ""

    def __init__(self):
        """ initializes City"""
        super(City, self).__init__()
