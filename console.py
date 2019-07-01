#!/usr/bin/python3
"""This module is the entry point of the command line interpreter"""


import cmd


from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand the interpreter"""

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, args):
        """method to create new instance of BaseModel"""
        if not args:
            print("** class name missing **")
        elif args not in storage.classes():
            print("** class doesn't exist **")
        else:
            new = eval(args)()
            new.save()
            print(new.id)

    def do_show(self):
        """method to print string representation of an instance"""

if __name__ == "__main__":
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
