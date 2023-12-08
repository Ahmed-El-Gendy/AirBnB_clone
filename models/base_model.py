#!/usr/bin/python3
"""
our base code
"""
import uuid
from datetime import datetime
#import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        tf = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for i, j in kwargs:
                if i == 'id':
                    self.__dict__[i] = str(j)
                elif i in ("created_at", "updated_at"):
                    self.__dict__[i] = datetime.strptime(j, tf)
                else:
                    self.__dict__[i] = j
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.utcnow()
            self.created_at = datetime.utcnow()
            #models.storage.new(self)

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
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        #models.storage.save()

    def ___str___(self):
        """
        print format
        """
        the_name = self.__class__.__name__
        the_dict = self.__dict__
        return "[{}] ({}) {}".format(the_name, self.id, the_dict)

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
