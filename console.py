#!/usr/bin/python3
"""This module is the entry point of the command line interpreter"""


import cmd


from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand the interpreter"""
    name = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Quit command to exit the program when EOF
        """
        print()
        return True

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
        if not cls:
            print("** class name missing **")
            return
        li = cls.split()
        if li[0] not in HBNBCommand.name:
            print("** class doesn't exist **")
        elif len(li) < 2:
            print("** instance id missing **")
        else:
            key = li[0] + "." + li[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, cls=None):
        """Deletes an instance based on the class name and id"""
        if not cls:
            print("** class name missing **")
            return
        li = cls.split()
        if li[0] not in HBNBCommand.name:
            print("** class doesn't exist **")
        elif len(li) < 2:
            print("** instance id missing **")
        else:
            key = li[0] + "." + li[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, cls=None):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        li = []
        d = storage.all()
        if not cls:
            for value in d.values():
                li.append(str(value))
            print(li)
        else:
            if cls in HBNBCommand.name:
                for key, value in d.items():
                    if key.split(".")[0] == cls:
                        li.append(str(value))
                print(li)
            else:
                print("** class doesn't exist **")

    def do_update(self, cls=None):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = cls.split()
        d = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.name:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in d:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if args[2] not in ["id", "created_at", "updated_at"]:
                for key, value in d.items():
                    if isint(args[3]) is True:
                        setattr(value, args[2], int(args[3]))
                    elif isfloat(args[3]) is True:
                        setattr(value, args[2], float(args[3]))
                    else:
                        setattr(value, args[2], args[3][1:-1])
                storage.save()

    def do_count(self, cls=None):
        """to retrieve the number of instances of a class"""
        if not cls:
            print("** class name missing **")
            return
        c = 0
        d = storage.all()
        if cls in HBNBCommand.name:
            for key, value in d.items():
                if key.split(".")[0] == cls:
                    c += 1
            print(c)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """default method if system doesn't recognize all command above"""
        l = line.split(".")
        if l[1] == "all()":
            return self.do_all(l[0])
        if l[1] == "count()":
            return self.do_count(l[0])
        if l[1][:4] == "show":
            a = l[1].split('"')
            name = l[0] + " " + a[1]
            return self.do_show(name)
        if l[1][:7] == "destroy":
            b = l[1].split('"')
            name_1 = l[0] + " " + b[1]
            return self.do_destroy(name_1)
        if l[1][:6] == "update":
            if not is_dict_representation(line):
                c = l[1].split(',')
                d = c[0].split("(")
                d_id = d[1][1:-1]
                n = l[0] + " " + d_id + " " + c[1][2:-1] + " " + c[2][1:-1]
                return self.do_update(n)
            else:
                c = l[1].split("(")
                d = c[1].split("{")
                e = eval("{" + d[1][:-1])
                for key, value in e.items():
                    new_value = value
                    if (isinstance(value, str)):
                        new_value = "'" + value + "'"
                    else:
                        new_value = str(value)
                    n = l[0] + " " + d[0][1:-3] + " " + key + " " + new_value
                    self.do_update(n)
                return


def isfloat(value):
    """check if the string can be converted to float"""
    try:
        float(value)
        return True
    except ValueError:
        return False


def isint(value):
    """check if the string can be converted to int"""
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_dict_representation(line):
    """to check if its dictionary representation"""
    l = line.split(".")
    c = l[1].split("(")
    for i in c[1][:-1]:
        if i is '{':
            return True
    return False


if __name__ == "__main__":
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
