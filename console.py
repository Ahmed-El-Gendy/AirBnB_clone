#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    the class
    """
    prompt = "(hbnb)"

    def end_of_file(self, arg):
        """
        handle EOF
        """
        print()
        return True

    def quit_app(self, arg):
        """
        handle quit
        """
        return True

    def quit_help(self, arg):
        """
        handle help quit
        """
        print("Quit command to exit the program")

if __name__ == "main__":
    HBNBCommand().cmdloop()
