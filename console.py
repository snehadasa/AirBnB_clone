#!/usr/bin/python3
"""entry point of the command line interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand the interpreter"""

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """empty line"""
        pass


if __name__ == "__main__":
    prompt = HBNBCommand()
    prompt.prompt = "(hbnb) "
    prompt.cmdloop()
