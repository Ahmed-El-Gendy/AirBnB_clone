#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import re
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """
    the class (cosole for web) new class
    saged ryan
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """
        handle EOF
        """
        print()
        return True

    def do_quit(self, arg):
        """
        handle quit
        """
        return True

    def help_quit(self):
        """
        handle help quit
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """ Do nothing"""
        pass

        def do_create(self, cls):
            """ create object from basemodel"""
            if not cls:
                print("** class name missing **")
                return
            if clc != "BaseModel":
                print("** class doesn't exist **")
                return
            new = eval(clc)()
            new.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
