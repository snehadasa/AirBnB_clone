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
        """Creates new instance of BaseModel, saves to JSON file, prints id"""
        if not args:
            print("** class name missing **")
            return
        try:
            new = eval(args)()
            new.save()
            print(new.id)
        except:
            print("** class doesn't exist **")

if __name__ == "__main__":
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
