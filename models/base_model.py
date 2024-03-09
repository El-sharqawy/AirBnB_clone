#!/usr/bin/python3
"""
Base Model Class
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """returns a string of the class data"""
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        return (string)

    def save(self):
        """Updates last time of the object"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a new dictionary copy of the original"""
        newDict = self.__dict__.copy()
        newDict["created_at"] = self.created_at.isoformat()
        newDict["updated_at"] = self.updated_at.isoformat()
        newDict["__class__"] = self.__class__.__name__
        return (newDict)
