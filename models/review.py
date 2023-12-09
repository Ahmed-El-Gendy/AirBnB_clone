#!/usr/bin/python3
""" new basemodel class the parent class """



from models.base_model import BaseModel



class Review(BaseModel):
    """ new  child class from basemodel class"""
    place_id = ""
    user_id = ""
    text = ""
