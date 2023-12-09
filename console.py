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
        if cls != "BaseModel":
            print("** class doesn't exist **")
            return
        new = eval(cls)()
        print(new.id)
        new.save()
    
    def do_show(self, args):
        """ show class str """
        if not args:
            print("** class name missing **")
            return
        li = args.split()
        if li[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(li) < 2:
            print("** instance id missing **")
            return
        ob = storage.all()
        data = f"{li[0]}.{li[1]}"
        if data in ob:
            print(ob[data])
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
