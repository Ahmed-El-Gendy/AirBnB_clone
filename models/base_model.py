#!/usr/bin/python3
"""
our base code
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """init the args and kwargs"""

        tf = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for i, j in kwargs.items():
                if i == 'id':
                    self.__dict__[i] = str(j)
                elif i in ("created_at", "updated_at"):
                    self.__dict__[i] = datetime.strptime(j, tf)
                elif i != "__class__":
                    self.__dict__[i] = j
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()

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

    def __str__(self):
        """
        print format
        """
        the_name = self.__class__.__name__
        the_dict = self.__dict__
        return "[{}] ({}) {}".format(the_name, self.id, self.__dict__)
