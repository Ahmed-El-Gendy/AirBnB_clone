#!/usr/bin/python3
"""
our base code the parent class
"""


import uuid
from datetime import datetime
from models


class BaseModel:
    """base model the partent class for user and city and other classes"""
    def __init__(self, *args, **kwargs):
        """init the args and kwargs"""

        tf = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i in ("created_at", "updated_at"):
                    self.__dict__[i] = datetime.strptime(j, tf)
                elif i == "__class__":
                    continue
                else:
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()
            models.storage.new(self)

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        ramy_dict = self.__dict__.copy()
        ramy_dict["__class__"] = self.__class__.__name__
        ramy_dict["created_at"] = self.created_at.isoformat()
        ramy_dict["updated_at"] = self.updated_at.isoformat()
        return ramy_dict

    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def __str__(self):
        """
        print format
        """
        the_name = self.__class__.__name__
        the_dict = self.__dict__
        return "[{}] ({}) {}".format(the_name, self.id, self.__dict__)
