#!/usr/bin/python3
"""The HBnB console."""

import cmd
import os
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
