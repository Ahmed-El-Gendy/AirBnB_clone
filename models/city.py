#!/usr/bin/python3
""" new module for class basemodel """

from models.base_model import BaseModel



class City(BaseModel):
    """ city  class inheret from base model class"""
    state_id = ""
    name = ""
