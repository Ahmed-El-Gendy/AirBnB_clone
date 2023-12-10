#!/usr/bin/python3
""" serialization-deserialization """


import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """ for file storage  new class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with
        key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ to the JSON file """
        serialized = {}
        for k, v in self.__objects.items():
            serialized[k] = v.to_dict()
        with open(self.__file_path, 'w+', encoding="utf-8") as f:
            json.dump(serialized, f)

    def reload(self):
        """ deserializes the JSON file """
        if not os.path.exists(FileStorage.__file_path):
            return
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
        except FileNotFoundError:
            pass
        except ValueError:
            pass
