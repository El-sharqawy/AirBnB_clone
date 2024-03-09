#!/usr/bin/python3
""" File Storage Class Impelementation"""

from models.base_model import BaseModel
import json
import models
import os


class FileStorage:
    """File Storage Class Variables"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """ creates an object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """ returns a dictionary contains all objects"""
        return (FileStorage.__objects)

    def save(self):
        """ serialize the class objects to JSON file"""
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized, file)

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
