#!/usr/bin/python3
""" serialization-deserialization """

import json
from models.base_model import BaseModel


class FileStorage:
    """ for file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with
        key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ to the JSON file """
        with open(self.__file_path, 'w+') as f:
            serialized = {}
            for k, v in self.__objects.items():
                serialized[k] = v.to_dict()
        json.dump(serialized, f)

    def reload(self):
        """ deserializes the JSON file """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.loads(f.read())
                for value in data.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
