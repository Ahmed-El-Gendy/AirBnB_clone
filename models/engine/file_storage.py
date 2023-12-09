#!/usr/bin/python3
""" serialization-deserialization """

import os
import json
from models.base_model import BaseModel


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
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    obj_instance = class_obj(**value)
                    self.__objects[key] = obj_instance
        else:
            return
