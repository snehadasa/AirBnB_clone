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
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, cls=None):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        a = ["BaseModel", "User"]
        if not cls:
            print("** class name missing **")
            return
        l = cls.split()
        if l[0] not in a:
            print("** class doesn't exist **")
        elif len(l) < 2:
            print("** instance id missing **")
        else:
            key = l[0] + "." + l[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, cls=None):
        """Deletes an instance based on the class name and id"""
        

if __name__ == "__main__":
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
