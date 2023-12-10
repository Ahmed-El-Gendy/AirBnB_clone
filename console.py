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
    my_list = ["BaseModel", "User", "Place", "State", "City", "Amenity"]

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
        if cls not in self.my_list:
            print("** class doesn't exist **")
            return
        new = eval(cls)()
        print(new.id)
        storage.save()

    def do_show(self, args):
        """ show class str """
        if not args:
            print("** class name missing **")
            return
        li = args.split()
        if li[0] not in self.my_list:
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

    def do_destroy(self, args):
        """ distroy the object"""
        if not args:
            print("** class name missing **")
            return
        li = args.split()
        if li[0] not in self.my_list:
            print("** class doesn't exist **")
            return
        if len(li) < 2:
            print("** instance id missing **")
            return
        ob = storage.all()
        data = f"{li[0]}.{li[1]}"
        if data in ob:
            del(ob[data])
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ print all instanses"""
        if not args:
            ob = storage.all()
            for i in ob.values():
                print(str(i))
            return
        s = args.split()
        if len(s) == 1:
            ob = storage.all()
            if s[0] not in self.my_list:
                print("** class doesn't exist **")
                return
            if s[0] == "BaseModel":
                for i, j in ob.items():
                    if i.split('.')[0] == "BaseModel":
                        print(str(j))
            elif s[0] == "User":
                for i, j in ob.items():
                    if i.split('.')[0] == "User":
                        print(str(j))
            elif s[0] == "Place":
                for i, j in ob.items():
                    if i.split('.')[0] == "Place":
                        print(str(j))
            elif s[0] == "State":
                for i, j in ob.items():
                    if i.split('.')[0] == "State":
                        print(str(j))
            elif s[0] == "City":
                for i, j in ob.items():
                    if i.split('.')[0] == "City":
                        print(str(j))
            elif s[0] == "Amenity":
                for i, j in ob.items():
                    if i.split('.')[0] == "Amenity":
                        print(str(j))
            elif s[0] == "Review":
                for i, j in ob.items():
                    if i.split('.')[0] == "Review":
                        print(str(j))

    def do_update(self, args):
        """update the attributes"""
        if not args:
            print("** class name missing **")
            return
        li = args.split()
        if li[0] not in self.my_list:
            print("** class doesn't exist **")
            return
        if len(li) < 2:
            print("** instance id missing **")
            return
        ob = storage.all()
        key = f"{li[0]}.{li[1]}"
        if key not in ob:
            print("** no instance found **")
            return
        if len(li) < 3:
            print("** attribute name missing **")
            return
        if len(li) < 4:
            print("** value missing **")
            return
        value = eval(li[3])
        setattr(ob[key], li[2], value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
