#!/usr/bin/python3
"""
Contain the class BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ base model used for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """ Prints the string representation of the BaseModel
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dtn = {x: y for (x, y) in self.__dict__.items() if (not y) is False}
        return class_name + "(" + self.id + ")" + str(dtn)

    def save(self):
        """
        Updates public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__
        """
        new_dict = {}
        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
