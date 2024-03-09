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
    prompt = "(hbnb) "
    classes = ["Amenity", "BaseModel", "City", "Place",
               "Review", "State", "User"]

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

    def do_create(self, arg):
        """creates a new instance of the given class,
        also print Class ID and the instance to the JSON file"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            newObj = eval(args[0])()
            newObj.save()
            print(newObj.id)

    def do_show(self, arg):
        """show all informations about specific class"""
        args = arg.split()
        myObjects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            myObj = "{}.{}".format(args[0], args[1])
            if myObj in myObjects:
                print(myObjects[myObj])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance of a specific class with ID"""
        args = arg.split()
        myObjects = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            myObject = "{}.{}".format(args[0], args[1])
            if myObject in myObjects:
                del myObjects[myObject]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """print all instances of given class"""
        objsList = []
        cls_name = arg.split()[0] if arg else None
        if cls_name and cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for object in storage.all().values():
                if not cls_name or cls_name == object.__class__.__name__:
                    objsList.append(str(object))
            print(objsList)

    def do_update(self, arg):
        """update instance based on given args"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        inID = args[1]
        objDict = storage.all()
        inKey = "{}.{}".format(cls_name, inID)
        if inKey not in objDict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        myObject = objDict[inKey]
        if hasattr(myObject, attr_name):
            setattr(myObject, attr_name, attr_value)
            myObject.save()
        else:
            setattr(myObject, attr_name, attr_value)
            myObject.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
