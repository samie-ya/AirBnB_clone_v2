#!/usr/bin/python3
"""Ths will create class BaseModel that defines all common attributes
/methods for other classes"""
import uuid
from datetime import datetime as date
from models import storage


class BaseModel:
    """This is the class base model"""

    def __init__(self, *args, **kwargs):
        """This is initialization of the class BaseModel

        Args:
            *args (tuple): This argument takes non-keyword arguments
            **kwargs (dic): This argument takes keyworded argumemnts
        """
        self.id = str(uuid.uuid4())
        self.created_at = date.now()
        self.updated_at = date.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at":
                    setattr(self, key, self.updated_at.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "created_at":
                    setattr(self, key, self.created_at.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """This will be the string representation of class name, the id,
           and dictionary when print or str is iused with the instance

        Returns:
            The string representation of class name, id and dictionary
        """
        return "[" + self.__class__.__name__ + "]" + " (" + self.id + ") \
" + str(self.__dict__)

    def save(self):
        """This function will update the public attribute update_at with the
           current time"""
        self.updated_at = date.now()
        storage.save()

    def to_dict(self):
        """This function will return a dictionary containing all key/value
           of dict

        Returns:
            The modified dictionary that contains the values of self.__dict__
        """
        x = {}
        x.update(self.__dict__)
        for key, value in x.items():
            if key == "created_at":
                x[key] = self.created_at.isoformat()
            if key == "updated_at":
                x[key] = self.updated_at.isoformat()
        x["__class__"] = self.__class__.__name__
        return x
