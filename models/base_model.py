#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""
"""


class BaseModel():
    """
    """

    def __init__(self, *args, **kwargs):
        """
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dtn = {x: y for (x, y) in self.__dict__.items() if (not y) is False}
        return class_name + "(" + self.id + ")" + str(dtn)

    def save(self):
        """
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
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