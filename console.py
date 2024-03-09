#!/usr/bin/python3
"""The HBnB console."""

import cmd
import os


class HBNBCommand(cmd.Cmd):
    """ the definition of HBnB command interperter"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program (ctrl+d)"""
        print("")
        return True

    def emptyline(self):
        """handle empty lines to print nothing"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
