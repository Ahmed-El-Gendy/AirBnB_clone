#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
