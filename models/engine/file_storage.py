#!/usr/bin/python3
""" File Storage Class Impelementation"""

import json
import models
import os


class FileStorage:
    """File Storage Class Variables"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns a dictionary contains all objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """ creates an object"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """ serialize the class objects to JSON file"""
        myObjects = FileStorage.__objects
        object_dictionary = {}
        for obj in myObjects.keys():
            object_dictionary[obj] = myObjects[obj].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(object_dictionary, file)

    def reload(self):
        """deserialize the JSON file to objects if it exists only."""
        try:
            with open(FileStorage.__file_path) as file:
                dictionary = json.load(file)
                for obj in dictionary.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
