#!/usr/bin/python3
"""
Contains the subclass Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ create an instance of a Review"""
    place_id = ""
    user_id = ""
    text = ""
